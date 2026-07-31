# Challenge 02: Obfuscated Entry

**Concept:** XOR Obfuscation / Dynamic Analysis
**Difficulty:** 🟢 Easy

## Objective
The player is given a compiled Linux binary (`vault_door.elf`). Running `strings` on it will not reveal the flag because the developer obfuscated it.

## Solution

### Method 1: Dynamic Analysis with `ltrace`
Even though the string is obfuscated at rest, the binary must de-obfuscate it in memory before comparing it against the user's input. The binary uses the standard C library function `strcmp` for the comparison. By dynamically tracing library calls using `ltrace`, we can intercept the de-obfuscated string.

```bash
$ ltrace ./vault_door.elf test
printf("Operation Black Vault - Vault Do"...Operation Black Vault - Vault Door Interface
) = 49
strcmp("test", "BVAULT{x0r_0bfu5c4710n_15_n07_3n"...) = 50
puts("Invalid Access Code. Vault Door "...Invalid Access Code. Vault Door remains locked.
) = 48
+++ exited (status 0) +++
```

### Method 2: Static Analysis (Ghidra / IDA)
By opening the binary in a decompiler like Ghidra, you will see a loop inside `main()`:
```c
  for (i = 0; i < 40; i = i + 1) {
    secret[i] = obfuscated[i] ^ 0x21;
  }
```
You can extract the hex bytes of the `obfuscated` array and write a quick Python script to XOR them against `0x21` to recover the flag.

## Flag
`BVAULT{x0r_0bfu5c4710n_15_n07_3ncryp710n}`
