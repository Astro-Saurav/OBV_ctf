# Miscellaneous — Organizer Manual

> **FOR ORGANIZERS ONLY** — This document contains solutions, flag values, and sandbox setup notes. Do not share with participants.

---

## Category Overview

| Field | Value |
|-------|-------|
| **Total Challenges** | 6 |
| **Difficulty Range** | 🟢 Easy → 🔴 Hard |
| **Format** | Mixed (Python PyJails, C sandboxes, polyglots, esoteric langs) |
| **Flag Format** | `BVAULT{...}` |
| **Deployment** | Mix of static files and live servers (PyJails) |

---

## Prerequisites

```bash
# Python sandbox / PyJail tools
sudo apt-get install -y python3 python3-pip ncat socat

# C sandbox compiler
sudo apt-get install -y gcc seccomp libseccomp-dev

# Esoteric language interpreters
sudo apt-get install -y beef        # Brainfuck
pip install malbolge-python         # Malbolge (optional)

# Steganography tools
sudo apt-get install -y steghide stegsolve zsteg
pip install stegano Pillow
```

---

## Challenge Reference

### Challenge 01 — The Decoy 🟢 Easy

| Field | Value |
|-------|-------|
| **Files** | Image file (`.png` / `.jpg`) |
| **Concept** | Steganography — LSB (Least Significant Bit) encoding |
| **Flag** | `BVAULT{d3c0y_1s_4_l13}` |

**Solve:**
```bash
steghide extract -sf decoy.jpg -p ""
# or
zsteg decoy.png
# or
python3 -c "
from PIL import Image
import numpy as np
img = np.array(Image.open('decoy.png'))
bits = img[:,:,0].flatten() & 1
chars = [''.join(map(str,bits[i:i+8])) for i in range(0,len(bits),8)]
print(''.join(chr(int(c,2)) for c in chars if int(c,2) > 31))
"
```

---

### Challenge 02 — Polyglot Paradox 🟡 Medium

| Field | Value |
|-------|-------|
| **Files** | `paradox.bin` — a valid PDF AND ZIP simultaneously |
| **Concept** | Polyglot file — valid in two different formats |
| **Flag** | `BVAULT{p0lygl0t_p4r4d0x_r3s0lv3d}` |

**Solve:**
```bash
# It's both a PDF and a ZIP
unzip paradox.bin        # Extract as ZIP → find flag.txt
# OR
file paradox.bin         # Identify both magic bytes
binwalk paradox.bin      # See both file systems
```

---

### Challenge 03 — The Chronos Anomaly 🟡 Medium

| Field | Value |
|-------|-------|
| **Files** | `timestamp_log.txt` + `anomaly.bin` |
| **Concept** | Time-based challenge — UNIX timestamp encoding + timezone manipulation |
| **Flag** | `BVAULT{chr0n0s_t1m3_4n0m4ly}` |

**Solve summary:** Timestamps in the log encode ASCII values when converted from specific timezone offsets.

---

### Challenge 04 — Terminal Echo 🟡 Medium

| Field | Value |
|-------|-------|
| **Format** | Live PyJail server |
| **Concept** | Python sandbox escape (restricted `__builtins__`) |
| **Flag** | `BVAULT{pyj41l_3sc4p3_3x3cut3d}` |
| **Port** | 7004 |

**Sandbox restrictions:**
```python
# Blocked: exec, eval, import, open, __import__, os, sys
# Allowed: print, len, str, int, list, dict
```

**Escape technique (one of several):**
```python
# Via subclass enumeration
().__class__.__mro__[-1].__subclasses__()[<index_of_os>]('cat flag.txt', shell=True, stdout=-1).communicate()
```

**Deploy:**
```bash
socat TCP-LISTEN:7004,fork,reuseaddr EXEC:"python3 pyjail.py"
```

**Verify solve:**
```bash
python3 test_exploit.py
```

---

### Challenge 05 — Schrödinger's Sandbox 🔴 Hard

| Field | Value |
|-------|-------|
| **Format** | Live C sandbox server (seccomp + fork) |
| **Concept** | C compiler sandbox — compile and run code with seccomp restrictions |
| **Flag** | `BVAULT{schr0d1ng3r_s4ndb0x_br0k3n}` |
| **Port** | 7005 |

**Allowed syscalls:** `read`, `write`, `exit`, `brk`, `mmap`, `mprotect`
**Blocked:** `execve`, `open`, `fork`, `socket`, `ptrace`

**Escape technique:** Use `openat` (not `open`) if not blocked, or ROP into allowed syscalls.

**Deploy:**
```bash
# Requires libseccomp
socat TCP-LISTEN:7005,fork,reuseaddr EXEC:"./sandbox_server"
```

---

### Challenge 06 — The Infinite Void 🔴 Hard

| Field | Value |
|-------|-------|
| **Files** | `void.bf` (Brainfuck program) |
| **Concept** | Esoteric programming — Brainfuck program hides flag in execution |
| **Flag** | `BVAULT{1nf1n1t3_v01d_tr4v3rs3d}` |

**Solve — run the Brainfuck program:**
```bash
# Install beef (Brainfuck interpreter)
sudo apt-get install beef
beef void.bf

# Or use Python:
python3 -c "
import sys
def bf(code, inp=''):
  tape, ptr, iptr, out = [0]*30000, 0, 0, []
  stack = []
  while iptr < len(code):
    c = code[iptr]
    if c == '>': ptr += 1
    elif c == '<': ptr -= 1
    elif c == '+': tape[ptr] = (tape[ptr]+1)%256
    elif c == '-': tape[ptr] = (tape[ptr]-1)%256
    elif c == '.': out.append(chr(tape[ptr]))
    elif c == '[':
      if tape[ptr]==0:
        d=1
        while d: iptr+=1; d+=code[iptr]=='['; d-=code[iptr]==']'
    elif c == ']':
      if tape[ptr]!=0:
        d=1
        while d: iptr-=1; d+=code[iptr]==']'; d-=code[iptr]=='['
    iptr+=1
  return ''.join(out)
print(bf(open('void.bf').read()))
"
```

---

## PyJail / Sandbox Server Deployment

### Ports Summary

| Challenge | Port | Type |
|-----------|------|------|
| challenge-04 | 7004 | Python PyJail |
| challenge-05 | 7005 | C seccomp sandbox |

### Start all live servers
```bash
# Challenge 04 - PyJail
socat TCP-LISTEN:7004,fork,reuseaddr EXEC:"python3 challenge-04-terminal-echo/pyjail.py" &

# Challenge 05 - Sandbox
socat TCP-LISTEN:7005,fork,reuseaddr EXEC:"./challenge-05-schrodingers-sandbox/sandbox_server" &

echo "Misc live servers running on ports 7004-7005"
```

---

## Common Participant Issues

| Issue | Solution |
|-------|---------|
| PyJail subclass index changes | Run `().__class__.__mro__[-1].__subclasses__()` to find correct index |
| Brainfuck program runs forever | It's supposed to — output appears before infinite loop |
| Seccomp sandbox crashes | Check `strace` to see which syscall is blocked |
| Steghide prompts for password | Try empty password first: `steghide extract -sf file -p ""` |
