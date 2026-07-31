# Challenge 03: Fast Prime

**Vulnerability / Concept:** RSA Small Exponent Attack (Cube Root Attack) + AES.
**Difficulty:** 🟡 Medium

## Objective
The player is provided with `encrypt.py` and `ciphertext.json`. The AES key was encrypted using RSA with `e=3`. Since the AES key is small (16 bytes = 128 bits) and `e=3`, the encrypted message $m^3$ is much smaller than the 2048-bit modulus $n$. Thus, the modular reduction $m^3 \pmod n$ never wrapped around. The player just needs to take the integer cube root of the ciphertext to recover the AES key, and then decrypt the AES-CBC flag.

## Solution

Because $m^3 < n$, the ciphertext $c = m^3 \pmod n$ is simply $c = m^3$ over the regular integers. We can recover $m$ by taking the exact integer cube root of $c$. 

### Exploit Script (`solve.py`)

```python
import json
import gmpy2
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open("ciphertext.json", "r") as f:
    data = json.load(f)

c_rsa = data["encrypted_aes_key"]
iv = bytes.fromhex(data["iv"])
c_aes = bytes.fromhex(data["encrypted_flag"])

# Cube Root Attack on RSA
# gmpy2.iroot(x, n) returns a tuple (root, exact_match_boolean)
m, exact = gmpy2.iroot(c_rsa, 3)
assert exact, "Cube root was not exact!"

aes_key = long_to_bytes(m)
print(f"[*] Recovered AES Key: {aes_key.hex()}")

# Decrypt AES-CBC
cipher = AES.new(aes_key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(c_aes), 16)

print(f"[+] Flag: {pt.decode()}")
```

### Execution
```bash
$ python3 solve.py
[*] Recovered AES Key: <hex>
[+] Flag: BVAULT{hybr1d_crypt0_w17h0ut_p4dd1ng_15_b4d}
```
