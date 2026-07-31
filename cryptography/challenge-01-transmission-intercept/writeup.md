# challenge-01-transmission-intercept

**Concept:** Multiple Encodings
**Difficulty:** 🟢 Easy

## Solution

The file `intercept.txt` contains a string that looks like Base64.
1. Base64 decode it to get a string of hex characters.
2. Hex decode it to get a Base32 string.
3. Base32 decode it to get the final flag.

```python
import base64
import binascii

with open("intercept.txt", "r") as f:
    data = f.read().strip()

# Layer 1: Base64
step1 = base64.b64decode(data)
# Layer 2: Hex (Base16)
step2 = binascii.unhexlify(step1)
# Layer 3: Base32
flag = base64.b32decode(step2)

print(flag.decode())
```

## Flag
`BVAULT{b453_3nc0d1ng_15_n07_3ncryp710n}`
