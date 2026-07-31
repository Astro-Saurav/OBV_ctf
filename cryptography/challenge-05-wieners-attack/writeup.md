# challenge-05-wieners-attack

**Concept:** RSA Wiener's Attack
**Difficulty:** 🔴 Hard

## Solution

When the private exponent `d` is chosen to be too small (specifically, less than `(1/3) * N^(1/4)`), it is vulnerable to Wiener's Attack. This attack uses the continued fraction expansion of `e/N` to find `d`.

You can use the popular python package `owiener` to automatically calculate `d`.

```python
# pip install owiener
import owiener
from Crypto.Util.number import long_to_bytes

# Load values from key.txt
N = ...
e = ...
c = ...

# Recover the private key d
d = owiener.attack(e, N)

if d is not None:
    # Decrypt
    m = pow(c, d, N)
    print(long_to_bytes(m).decode())
else:
    print("Wiener's attack failed.")
```

## Flag
`BVAULT{w13n3r5_4774ck_r54_br0k3n}`
