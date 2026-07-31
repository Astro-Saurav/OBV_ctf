# challenge-04-repeating-xor

**Concept:** Repeating Key XOR
**Difficulty:** 🟡 Medium

## Solution

The encryption is a repeating-key XOR. Since we know the first 19 bytes of the plaintext (`SYSTEM STATUS REPORT:`), we can simply XOR the beginning of the ciphertext with the known plaintext to recover the repeating key.

```python
with open("encrypted.bin", "rb") as f:
    ct = f.read()

known_pt = b"SYSTEM STATUS REPORT:"
# XOR ciphertext with known plaintext to find the key
key = bytes([ct[i] ^ known_pt[i] for i in range(6)])
print(f"Recovered Key: {key}")

# Decrypt the full message
pt = bytes([ct[i] ^ key[i % len(key)] for i in range(len(ct))])
print(pt.decode())
```

## Flag
`BVAULT{r3p3471ng_x0r_k3y_br0k3n}`
