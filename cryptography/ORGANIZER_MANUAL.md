# Cryptography — Organizer Manual

> **FOR ORGANIZERS ONLY** — This document contains solutions, flag values, and key material. Do not share with participants.

---

## Category Overview

| Field | Value |
|-------|-------|
| **Total Challenges** | 8 (including legacy challenges) |
| **Difficulty Range** | 🟢 Easy → 🔴 Hard |
| **Format** | Python scripts + encrypted artifacts |
| **Flag Format** | `BVAULT{...}` |
| **Deployment** | Static files (no server required) |

---

## Prerequisites

```bash
# Install Python crypto libraries
pip install pycryptodome gmpy2 sympy

# Optional: SageMath for advanced number theory
# https://www.sagemath.org/download.html
```

---

## Challenge Reference

### Challenge 01 — Transmission Intercept 🟢 Easy (100 pts)

| Field | Value |
|-------|-------|
| **Files** | `intercept.txt` |
| **Concept** | Base64 + Caesar cipher (ROT13 layer) |
| **Flag** | `BVAULT{tr4nsm1ss10n_1nt3rc3pt3d}` |

**Solve summary:** Decode Base64, then apply ROT13.

**Regenerate:**
```bash
python3 -c "
import base64
msg = 'BVAULT{tr4nsm1ss10n_1nt3rc3pt3d}'
# Apply ROT13 then Base64
import codecs
enc = base64.b64encode(codecs.encode(msg, 'rot_13').encode()).decode()
print(enc)
" > intercept.txt
```

---

### Challenge 01 — Phantom Shift 🟢 Easy (200 pts)

| Field | Value |
|-------|-------|
| **Files** | `file/encrypt.py`, `file/intercept.txt`, `file.zip` |
| **Concept** | Vigenère cipher with known key structure |
| **Flag** | `BVAULT{v1g3n3r3_k3y_r3c0v3r3d}` |

**Key used:** `PHANTOM`

**Solve summary:** Frequency analysis or known-plaintext attack on Vigenère with key length 7.

**Regenerate:**
```bash
cd challenge-01-phantom-shift/file
python3 encrypt.py
zip -r ../file.zip .
```

---

### Challenge 02 — Shifted Orders 🟢 Easy (200 pts)

| Field | Value |
|-------|-------|
| **Files** | `message.txt` |
| **Concept** | XOR with single-byte key |
| **Flag** | `BVAULT{s1ngl3_byt3_xor_cr4ck3d}` |
| **Key** | `0x42` |

---

### Challenge 02 — Single Vector 🟡 Medium (400 pts)

| Field | Value |
|-------|-------|
| **Files** | `file/encrypt.py`, `file/encrypted_doc.bin`, `file.zip` |
| **Concept** | Single-byte XOR brute force over binary blob |
| **Flag** | `BVAULT{xor_v3ct0r_3xp0s3d}` |

**Solve summary:** Try all 256 possible single-byte keys, identify correct one by checking for flag prefix.

---

### Challenge 03 — Weak RSA 🟡 Medium (500 pts)

| Field | Value |
|-------|-------|
| **Files** | `public.txt` |
| **Concept** | RSA with small public exponent (e=3), no padding |
| **Flag** | `BVAULT{w34k_rsa_3xp0n3nt_d3f34t3d}` |

**Key parameters:**
- `e = 3`
- `n` = 2048-bit modulus
- `c = m^3 mod n` with `m^3 < n` → direct cube root

**Solve:**
```python
import gmpy2
c = int(open('public.txt').read().split('\n')[1], 16)
m, exact = gmpy2.iroot(c, 3)
print(bytes.fromhex(hex(m)[2:]).decode())
```

---

### Challenge 03 — Fast Prime 🟡 Medium (600 pts)

| Field | Value |
|-------|-------|
| **Files** | `file/encrypt.py`, `file/ciphertext.json`, `file.zip` |
| **Concept** | RSA with weak prime generation (small prime difference) |
| **Flag** | `BVAULT{f4st_pr1m3_f4ct0r3d}` |

**Vulnerability:** `p` and `q` generated too close together → Fermat factorisation.

**Regenerate:**
```bash
cd challenge-03-fast-prime/file
python3 encrypt.py
zip -r ../file.zip .
```

---

### Challenge 04 — Repeating XOR 🟡 Medium (600 pts)

| Field | Value |
|-------|-------|
| **Files** | `encrypted.bin` |
| **Concept** | Repeating-key XOR (Kasiski / IC method) |
| **Flag** | `BVAULT{r3p34t1ng_xor_k3y_r3c0v3r3d}` |
| **Key length** | 12 bytes |

---

### Challenge 04 — Predictable Future 🔴 Hard (900 pts)

| Field | Value |
|-------|-------|
| **Files** | `file/encrypt.py`, `file/captured_data.json`, `file.zip` |
| **Concept** | LCG (Linear Congruential Generator) keystream prediction |
| **Flag** | `BVAULT{lcg_pr3d1ct3d_th3_futur3}` |

**Solve summary:** Given consecutive LCG outputs, recover `a`, `c`, `m` parameters and predict future outputs.

---

### Challenge 05 — Wiener's Attack 🔴 Hard (1000 pts)

| Field | Value |
|-------|-------|
| **Files** | `key.txt` |
| **Concept** | RSA Wiener's Attack (large `e`, small `d`) |
| **Flag** | `BVAULT{w13n3r_att4ck_succ3ssful}` |

**Solve summary:** Use continued fractions on `e/n` to find `d` when `d < n^0.25`.

---

### Challenge 06 — Mersenne Twister 🔴 Hard (1200 pts)

| Field | Value |
|-------|-------|
| **Concept** | MT19937 PRNG state recovery from 624 consecutive outputs |
| **Flag** | `BVAULT{m3rs3nn3_tw1st3r_unr4v3l3d}` |

**Solve summary:** Collect 624 32-bit outputs, untemper each, set MT state, predict future values.

---

## Verifying All Flags

```bash
# Run all solve scripts and check output
for ch in challenge-*/; do
  echo "=== $ch ==="
  cd "$ch"
  python3 test_exploit.py 2>/dev/null | grep -oP 'BVAULT\{[^}]+\}' || echo "NO FLAG FOUND"
  cd ..
done
```

---

## Common Participant Issues

| Issue | Solution |
|-------|---------|
| `gmpy2` not installed | `pip install gmpy2` |
| RSA solve takes too long | Hint: check if `m^e < n` (no reduction needed) |
| LCG params unknown | Hint: parameters are in `encrypt.py` source |
| MT state recovery off | Ensure exactly 624 consecutive 32-bit outputs are collected |
