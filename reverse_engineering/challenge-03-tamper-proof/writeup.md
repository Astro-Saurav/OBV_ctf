# Challenge 03: Tamper Proof

**Concept:** Anti-Debugging (`ptrace`) & Dynamic Flag Generation
**Difficulty:** 🟡 Medium

## Objective
The player is given a compiled Linux binary (`drone_uplink.elf`). It expects an activation code integer. If the player tries to use `ltrace` or `gdb` on it, the binary detects the debugger and prints a fake flag.

## Solution

### 1. Reversing the Logic
By opening the binary in a decompiler (like Ghidra), we can examine the `main` function.
We find the following logic:
```c
  int code = atoi(argv[1]);
  if ((code ^ 0x1337) != 0xdead) {
    puts("Access Denied.");
    return 1;
  }
```
This tells us the correct activation code.
`code ^ 0x1337 = 0xdead`
Therefore, `code = 0xdead ^ 0x1337 = 0xcd9a = 52634`.

### 2. The Anti-Debugging Trap
If you run the binary with `ltrace ./drone_uplink.elf 52634`, you get a fake flag:
`BVAULT{f4k3_fl4g_y0u_4r3_b31ng_w47ch3d}`

Looking deeper into the decompiler, we see:
```c
  if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
    print_flag(fake_enc, 40, code);
    return 1;
  }
  print_flag(real_enc, 38, code);
```
The `ptrace` call is a classic Linux anti-debugging trick. If a process is already being traced (e.g., by `gdb` or `ltrace`), `ptrace(PTRACE_TRACEME)` will fail and return `-1`. 

Because the binary detects the debugger, it branches to the fake flag output!

### 3. Execution
To get the real flag, simply run the binary normally without a debugger attached, using the activation code we calculated.

```bash
$ ./drone_uplink.elf 52634
Drone Uplink Interface
Access Granted. Flag: BVAULT{4n71_d3bugg1ng_w17h_p7r4c3}
```

Alternatively, you can patch the binary to replace the `ptrace` check with a NOP, or patch the conditional jump (e.g. change `JZ` to `JMP`) using a hex editor, but simply running it outside the debugger is the easiest solution.

## Flag
`BVAULT{4n71_d3bugg1ng_w17h_p7r4c3}`
