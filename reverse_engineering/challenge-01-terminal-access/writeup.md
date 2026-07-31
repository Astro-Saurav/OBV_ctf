# Challenge 01: Terminal Access

**Concept:** Hardcoded Strings
**Difficulty:** 🟢 Easy

## Objective
The player is given a compiled Linux binary (`auth_module.elf`). When executed, it asks for an access code. The goal is to find the hardcoded access code.

## Solution
This is a classic introductory Reverse Engineering challenge. The developer hardcoded the password directly into the source code, which means it exists as a plaintext string inside the compiled binary's `.rodata` (read-only data) section.

### Method 1: Using `strings`
The easiest way to solve this is to use the `strings` utility on Linux, which extracts printable character sequences from a binary file.

```bash
$ strings auth_module.elf | grep BVAULT
BVAULT{h4rdc0d3d_57r1ng5_4r3_b4d}
```

### Method 2: Dynamic Analysis with `ltrace`
Alternatively, you can run the binary and trace library calls using `ltrace`. The binary uses `strcmp` to compare your input with the secret password.

```bash
$ ltrace ./auth_module.elf test_password
printf("Operation Black Vault - Terminal"...Operation Black Vault - Terminal Access
) = 40
strcmp("test_password", "BVAULT{h4rdc0d3d_57r1ng5_4r3_b4d}") = 116
puts("Access Denied."Access Denied.
) = 15
+++ exited (status 0) +++
```
The second argument to `strcmp` reveals the flag.

## Flag
`BVAULT{h4rdc0d3d_57r1ng5_4r3_b4d}`
