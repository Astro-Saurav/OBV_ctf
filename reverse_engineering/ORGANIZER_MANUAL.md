# Reverse Engineering — Organizer Manual

> **FOR ORGANIZERS ONLY** — This document contains solutions, flag values, and binary analysis notes. Do not share with participants.

---

## Category Overview

| Field | Value |
|-------|-------|
| **Total Challenges** | 6 |
| **Difficulty Range** | 🟢 Easy → 🔴 Hard |
| **Format** | Stripped ELF binaries (x86-64 Linux) |
| **Flag Format** | `BVAULT{...}` |
| **Deployment** | Static binary distribution (no server) |

---

## Prerequisites / Recommended Tools

```bash
# Disassemblers / Decompilers
# - Ghidra (free): https://ghidra-sre.org/
# - Binary Ninja (free tier): https://binary.ninja/
# - IDA Free: https://hex-rays.com/ida-free/

# CLI tools
sudo apt-get install -y \
  gdb ltrace strace \
  radare2 \
  binutils \
  python3-pip

pip install keystone-engine capstone unicorn

# GDB plugins
bash -c "$(curl -fsSL https://gef.blah.cat/sh)"  # GEF
```

---

## Challenge Reference

### Challenge 01 — Terminal Access 🟢 Easy

| Field | Value |
|-------|-------|
| **Binary** | stripped ELF (no symbols) |
| **Concept** | Static string analysis — hardcoded password comparison |
| **Technique** | `strings`, `ltrace`, basic Ghidra decompile |
| **Flag** | `BVAULT{t3rm1n4l_4cc3ss_gr4nt3d}` |

**Quick solve:**
```bash
strings terminal_access.elf | grep BVAULT
# or
ltrace ./terminal_access.elf
```

---

### Challenge 02 — Obfuscated Entry 🟢 Easy

| Field | Value |
|-------|-------|
| **Binary** | stripped ELF with XOR-obfuscated strings |
| **Concept** | String obfuscation — XOR decode at runtime |
| **Technique** | Dynamic analysis with GDB / `strace` |
| **Flag** | `BVAULT{0bfusc4t3d_3ntry_cl34r3d}` |

**Solve with strace:**
```bash
strace ./obfuscated_entry.elf 2>&1 | grep write
```

**GDB approach:**
```bash
gdb ./obfuscated_entry.elf
# break at strcmp or puts, examine arguments
```

---

### Challenge 03 — Tamper Proof 🟡 Medium

| Field | Value |
|-------|-------|
| **Binary** | ELF with anti-debugging (ptrace check, timing checks) |
| **Concept** | Bypass anti-debug techniques |
| **Technique** | Patch binary, LD_PRELOAD hook, or GDB script |
| **Flag** | `BVAULT{t4mp3r_pr00f_byp4ss3d}` |

**Bypass ptrace check:**
```bash
# Patch the ptrace call in binary (NOP the jump)
# or use LD_PRELOAD to fake ptrace return value
cat > fake_ptrace.c << 'EOF'
#include <sys/ptrace.h>
long ptrace(enum __ptrace_request req, ...) { return 0; }
EOF
gcc -shared -fPIC -o fake_ptrace.so fake_ptrace.c
LD_PRELOAD=./fake_ptrace.so ./tamper_proof.elf
```

---

### Challenge 04 — Serial Interface 🟡 Medium

| Field | Value |
|-------|-------|
| **Binary** | Custom serial key validation |
| **Concept** | Keygen — reverse the serial validation algorithm |
| **Technique** | Ghidra decompile → understand checksum → generate valid key |
| **Flag** | `BVAULT{s3r14l_1nt3rf4c3_k3yg3n}` |

**Valid serial format:** `XXXX-XXXX-XXXX-XXXX` (checksum-based)

---

### Challenge 05 — The Ghost VM 🔴 Hard

| Field | Value |
|-------|-------|
| **Binary** | `ghost_vm.elf` + `vault_logic.bin` |
| **Concept** | Custom Virtual Machine architecture with 12 opcodes |
| **Technique** | Implement VM interpreter in Python, trace execution |
| **Flag** | `BVAULT{gh0st_vm_0pc0d3_m4st3r}` |

**VM Architecture:**
- 8 general-purpose registers (R0–R7)
- 4 opcodes for arithmetic, 3 for control flow, 3 for I/O, 2 for memory
- `vault_logic.bin` = bytecode for the VM to execute

**Approach:**
1. Reverse `ghost_vm.elf` to understand opcode dispatch table
2. Write Python VM emulator
3. Trace `vault_logic.bin` execution to extract flag

---

### Challenge 06 — Deep Root 🔴 Hard

| Field | Value |
|-------|-------|
| **Binary** | `backdoor_daemon.elf` + `recovered_sys.log` |
| **Concept** | Backdoor analysis — custom C2 protocol + crypto |
| **Technique** | Network protocol reversing + decrypt C2 traffic using log keys |
| **Flag** | `BVAULT{d33p_r00t_b4ckd00r_3xp0s3d}` |

**Solve summary:**
1. Reverse `backdoor_daemon.elf` to find C2 protocol (custom XOR + RC4)
2. Extract session key from `recovered_sys.log`
3. Decrypt C2 traffic to reveal flag

---

## Compilation Reference

All binaries were compiled on **Ubuntu 22.04, GCC 11.4**, x86-64:

```bash
# Easy (minimal stripping)
gcc -O1 -s -o <binary>.elf <source>.c

# Medium (full stripping + optimization)
gcc -O2 -s -fno-ident -o <binary>.elf <source>.c

# Hard (full stripping + obfuscation + static link)
gcc -O3 -s -fno-ident -static -o <binary>.elf <source>.c
strip --strip-all <binary>.elf
```

---

## Running All Solve Scripts

```bash
for ch in challenge-*/; do
  echo "=== Testing $ch ==="
  cd "$ch"
  timeout 30 python3 test_exploit.py 2>/dev/null | grep -oP 'BVAULT\{[^}]+\}' \
    || timeout 30 bash test_exploit.sh 2>/dev/null | grep -oP 'BVAULT\{[^}]+\}' \
    || echo "FAILED / TIMEOUT"
  cd ..
done
```

---

## Common Participant Issues

| Issue | Solution |
|-------|---------|
| Binary won't run | `chmod +x *.elf` and check architecture: `file *.elf` |
| Ghidra hangs on analysis | Increase JVM heap: `-Xmx4g` in `ghidraRun` |
| Anti-debug crashes binary | Use `LD_PRELOAD` ptrace hook (see challenge-03) |
| VM opcode table not found | Search for large switch-case block in Ghidra |
