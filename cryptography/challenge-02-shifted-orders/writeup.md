# challenge-02-shifted-orders

**Concept:** Vigenere Cipher
**Difficulty:** 🟢 Easy

## Solution

This is a classic Vigenere cipher using the key `VAULT`. 
You can use an online tool like CyberChef, or write a simple Python script.

```python
def vigenere_decrypt(text, key):
    res = []
    k_idx = 0
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            k = ord(key[k_idx % len(key)].upper()) - ord('A')
            res.append(chr((ord(c) - base - k) % 26 + base))
            k_idx += 1
        else:
            res.append(c)
    return "".join(res)

with open("message.txt", "r") as f:
    ct = f.read()
    
print(vigenere_decrypt(ct, "VAULT"))
```

## Flag
`BVAULT{v1g3n3r3_c1ph3r_ccl4551c}`
