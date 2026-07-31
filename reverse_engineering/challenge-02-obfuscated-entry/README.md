# 2 Obfuscated Entry

**Category:** Reverse Engineering
**Difficulty:** 🟢 Easy

## Description
Operation Black Vault — Reverse Engineering
Challenge: Obfuscated Entry
Difficulty: 🟢 Easy

The vault engineers tried to hide their credentials using a custom obfuscation routine, thinking it would defeat basic string scanners.

Find the access code to unlock the vault door.

---
*Note for Platform Upload:*
**Flag:** `BVAULT{x0r_0bfu5c4710n_15_n07_3n"...) = 50
puts("Invalid Access Code. Vault Door "...Invalid Access Code. Vault Door remains locked.
) = 48
+++ exited (status 0) +++
```

### Method 2: Static Analysis (Ghidra / IDA)
By opening the binary in a decompiler like Ghidra, you will see a loop inside `main()`:
```c
  for (i = 0; i < 40; i = i + 1) {
    secret[i] = obfuscated[i] ^ 0x21;
  }`
