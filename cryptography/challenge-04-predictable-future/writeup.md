# Challenge 04: Predictable Future

**Vulnerability / Concept:** Custom LCG (Linear Congruential Generator) Cracking + DES.
**Difficulty:** 🟡 Medium

## Objective
The player is provided with `encrypt.py` and `captured_data.json`. The flag is XOR'd with an LCG keystream and then DES encrypted. The DES key is hardcoded. The LCG multiplier `a` and increment `c` are unknown, but the modulus `m` and three consecutive outputs $X_1, X_2, X_3$ are given.

## Solution

1. **Decrypt DES:** Since the DES key is provided (`V4ULTK3Y`), we just decrypt the hex payload using `pycryptodome` DES in ECB mode and unpad it. This gives us the XOR ciphertext.
2. **Crack the LCG:** We have:
   $X_2 = (a X_1 + c) \pmod m$
   $X_3 = (a X_2 + c) \pmod m$
   Subtracting them: $X_3 - X_2 \equiv a (X_2 - X_1) \pmod m$
   Since $m$ is prime, we can find the modular inverse of $(X_2 - X_1)$ modulo $m$, allowing us to solve for $a$.
   Once $a$ is found, $c = (X_2 - a X_1) \pmod m$.
3. **Generate Keystream:** With $a, c, m$ known, we generate $X_4, X_5 \dots$ and pack them as 32-bit integers to form the keystream, then XOR it with the decrypted DES payload to get the flag.

### Exploit Script (`solve.py`)

```python
import json
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import inverse

with open("captured_data.json", "r") as f:
    data = json.load(f)

m = data["m"]
x1, x2, x3 = data["tokens"]
des_key = data["des_key"].encode()
des_cipher = bytes.fromhex(data["encrypted_flag"])

# Step 1: Decrypt DES
cipher = DES.new(des_key, DES.MODE_ECB)
xor_cipher = unpad(cipher.decrypt(des_cipher), 8)

# Step 2: Crack LCG
# (x3 - x2) = a * (x2 - x1) mod m
diff_32 = (x3 - x2) % m
diff_21 = (x2 - x1) % m
inv_diff_21 = inverse(diff_21, m)

a = (diff_32 * inv_diff_21) % m
c = (x2 - a * x1) % m

print(f"[*] Found a: {a}")
print(f"[*] Found c: {c}")

# Step 3: Generate keystream
seed = x3
keystream = b""
while len(keystream) < len(xor_cipher):
    seed = (a * seed + c) % m
    keystream += seed.to_bytes(4, 'big')

keystream = keystream[:len(xor_cipher)]

# Step 4: XOR
flag = bytes([f ^ k for f, k in zip(xor_cipher, keystream)])
print(f"[+] Flag: {flag.decode()}")
```

### Execution
```bash
$ python3 solve.py
[*] Found a: 1103515245
[*] Found c: 12345
[+] Flag: BVAULT{pr3d1c71ng_7h3_lcg_k3y57r34m}
```
