# Challenge 02: Single Vector

**Vulnerability / Concept:** Hybrid substitution and XOR.
**Difficulty:** 🟢 Easy

## Objective
The player is provided with `encrypted_doc.bin` and the `encrypt.py` script. They must reverse the Base32 encoding, reverse the custom substitution cipher, and brute-force (or determine) the single-byte XOR key.

## Solution

The encryption script shows the exact process:
`Flag -> Single-byte XOR -> Custom Substitution -> Base32`

To solve it, we perform the inverse operations in reverse order:
1. Decode Base32.
2. Reverse the substitution by translating the bytes back using a reversed translation table.
3. Brute force the single-byte XOR key (or since we know the flag format is `BVAULT{...}`, we can XOR the first byte with `B` to instantly find the key: `0x42`).

### Exploit Script (`solve.py`)

```python
import base64

with open("encrypted_doc.bin", "rb") as f:
    layer3 = f.read()

# Reverse Layer 3: Base32
layer2 = base64.b32decode(layer3)

# Reverse Layer 2: Custom Substitution
plain = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}_"
cipher = b"QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm9876543210_}{"

reverse_table = bytes.maketrans(cipher, plain)
layer1 = layer2.translate(reverse_table)

# Reverse Layer 1: Single-byte XOR
# We know the flag starts with 'B', so: key = layer1[0] ^ ord('B')
key = layer1[0] ^ ord('B')
print(f"[*] Recovered XOR key: 0x{key:02x}")

flag = bytes([c ^ key for c in layer1]).decode()
print(f"[+] Flag: {flag}")
```

### Execution
```bash
$ python3 solve.py
[*] Recovered XOR key: 0x42
[+] Flag: BVAULT{x0r_m45k_4nd_5ub5717u710n_br0k3n}
```
