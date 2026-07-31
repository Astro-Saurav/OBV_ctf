# Challenge 01: Phantom Shift

**Vulnerability / Concept:** Multi-layered encoding & classic cipher (Vigenere + Base64 + ROT13 + Hex).
**Difficulty:** 🟢 Easy

## Objective
The player is given `intercept.txt` and a hint in the description ("PHANTOM"). They must reverse a sequence of basic encodings and a Vigenere cipher to extract the flag.

## Solution

The encryption flow is:
`Flag -> Vigenere (key="PHANTOM") -> Base64 -> ROT13 -> Hexadecimal`

To solve it, we just reverse the layers:
1. Decode from Hex to ASCII.
2. Decode ROT13.
3. Decode Base64.
4. Decrypt Vigenere using the key `PHANTOM`.

### Exploit Script (`solve.py`)

```python
import binascii
import codecs
import base64

with open("intercept.txt", "r") as f:
    hex_data = f.read().strip()

# Layer 1: Hex to ASCII
rot_data = binascii.unhexlify(hex_data).decode()

# Layer 2: ROT13
b64_data = codecs.decode(rot_data, 'rot_13')

# Layer 3: Base64
vigenere_data = base64.b64decode(b64_data).decode()

# Layer 4: Vigenere Decrypt (Key = PHANTOM)
key = "PHANTOM"
res = []
key_idx = 0
for char in vigenere_data:
    if char.isalpha():
        shift = ord(key[key_idx % len(key)].upper()) - 65
        if char.isupper():
            res.append(chr((ord(char) - 65 - shift) % 26 + 65))
        else:
            res.append(chr((ord(char) - 97 - shift) % 26 + 97))
        key_idx += 1
    else:
        res.append(char)

flag = "".join(res)
print(f"[+] Flag: {flag}")
```

### Execution
```bash
$ python3 solve.py
[+] Flag: BVAULT{l4y3r5_0f_0b5cur17y_f41l}
```
