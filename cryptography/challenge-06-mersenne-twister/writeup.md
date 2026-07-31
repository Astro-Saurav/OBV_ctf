# challenge-06-mersenne-twister

**Concept:** Mersenne Twister PRNG Predict
**Difficulty:** 🔴 Hard

## Solution

Python's `random` module uses the Mersenne Twister (MT19937) algorithm. 
MT19937 has an internal state of 624 32-bit integers. If you can observe 624 consecutive outputs, you can perfectly reconstruct the internal state and predict all future random numbers.

Using the `randcrack` library, we can feed it the 624 leaked integers, and then use it to generate the exact same keys that were used to encrypt the flag via XOR.

```python
# pip install randcrack
from randcrack import RandCrack
import struct

rc = RandCrack()

with open("leak.txt", "r") as f:
    for line in f:
        val = int(line.strip())
        rc.submit(val)

with open("encrypted_flag.bin", "rb") as f:
    enc_flag = f.read()

pt = bytearray()
for i in range(0, len(enc_flag), 4):
    block = struct.unpack("<I", enc_flag[i:i+4])[0]
    key = rc.predict_getrandbits(32)
    pt.extend(struct.pack("<I", block ^ key))

print(pt.decode('utf-8', 'ignore'))
```

## Flag
`BVAULT{m3r53nn3_7w1573r_prng_c0mpr0m153d}`
