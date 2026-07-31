# challenge-03-weak-rsa

**Concept:** RSA Small Exponent (Cube Root Attack)
**Difficulty:** 🟡 Medium

## Solution

Because the public exponent `e` is extremely small (e = 3) and the message `m` is relatively small, the message was not padded. This means that `m^3` is strictly less than the modulus `N`.
As a result, the modulo `N` operation doesn't actually wrap around, and we can simply take the regular integer cube root of `c` to recover `m`.

```python
import gmpy2
from Crypto.Util.number import long_to_bytes

# Load values from public.txt
N = ... 
c = ...

# Take the integer cube root
m, exact = gmpy2.iroot(c, 3)

if exact:
    print(long_to_bytes(m).decode())
```

## Flag
`BVAULT{r54_5m4ll_3_c0mm0n_m1574k3}`
