# 3 Fast Prime

**Category:** Cryptography
**Difficulty:** 🟡 Medium

## Description
Operation Black Vault — Cryptography
Challenge: Fast Prime
Difficulty: 🟡 Medium

The enemy engineer tried to securely send an AES key to a field agent using RSA. However, to optimize encryption speed on their low-power field radios, they used a very small public exponent (e=3) and neglected to use any padding. 

We recovered the `ciphertext.json` and the `encrypt.py` script.
Break the RSA encryption to recover the AES key, then decrypt the flag.

## Files to Provide to Players
- `encrypt.py`
- `ciphertext.json`

---
*Note for Platform Upload:*
**Flag:** `BVAULT{hybr1d_crypt0_w17h0ut_p4dd1ng_15_b4d}`
