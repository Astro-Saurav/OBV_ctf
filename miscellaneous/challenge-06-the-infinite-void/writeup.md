# Challenge 06: The Infinite Void

**Concept:** Steganography using Zero-Width Characters
**Difficulty:** 🟠 Medium

## Objective
Players are given a text file, `void.txt`, that appears to contain only a single sentence:
"The void contains nothing. Do not stare too long."
The goal is to find the hidden flag inside the text.

## Solution
If players examine the file size or open it in a hex editor (or a text editor that reveals hidden characters), they will notice that the file is significantly larger than the visible characters.
The file contains a large number of **Zero-Width Characters** hidden immediately after the first character 'T'.

Specifically, it uses two unicode characters to encode binary data:
- `U+200B` (Zero-Width Space) represents the binary bit `0`.
- `U+200C` (Zero-Width Non-Joiner) represents the binary bit `1`.

By reading the file in Python (or any other language) and parsing these characters back into binary strings (chunked by 8 bits), players can decode the ASCII characters of the flag.

### Decode Script
```python
def decode_flag(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    binary = ""
    for c in content:
        if c == '\u200B':
            binary += '0'
        elif c == '\u200C':
            binary += '1'
            
    # Group by 8 bits and convert to ASCII
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    flag = "".join(chars)
    print("Flag:", flag)

if __name__ == "__main__":
    decode_flag("void.txt")
```

## Flag
`BVAULT{z3r0_w1dth_ch4r4ct3r5_4r3_1nv151bl3}`
