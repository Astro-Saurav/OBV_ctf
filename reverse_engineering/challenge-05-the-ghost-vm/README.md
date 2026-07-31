# 5 The Ghost Vm

**Category:** Reverse Engineering
**Difficulty:** 🔴 Hard

## Description
Operation Black Vault — Reverse Engineering
Challenge: The Ghost VM
Difficulty: 🔴 Hard

The Black Vault doesn't execute standard x86 binaries for its most critical operations. Instead, it runs a proprietary, lightweight Virtual Machine. We extracted the VM engine (ghost_vm.elf) and a raw bytecode payload (vault_logic.bin).

Reverse the VM engine to understand the custom Instruction Set Architecture, then decompile the bytecode to find the access code.

Usage: ./ghost_vm.elf <access_code>

---
*Note for Platform Upload:*
**Flag:** `BVAULT{gh057_vm_r3v3r53d_5ucc355fully}`
