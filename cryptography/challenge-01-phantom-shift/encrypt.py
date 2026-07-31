import base64
import codecs
import binascii

flag = "BVAULT{l4y3r5_0f_0b5cur17y_f41l}"
key = "PHANTOM"

def vigenere_encrypt(text, key):
    res = []
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)].upper()) - 65
            if char.isupper():
                res.append(chr((ord(char) - 65 + shift) % 26 + 65))
            else:
                res.append(chr((ord(char) - 97 + shift) % 26 + 97))
            key_idx += 1
        else:
            res.append(char)
    return "".join(res)

# Layer 1: Vigenere
layer1 = vigenere_encrypt(flag, key)

# Layer 2: Base64
layer2 = base64.b64encode(layer1.encode()).decode()

# Layer 3: ROT13
layer3 = codecs.encode(layer2, 'rot_13')

# Layer 4: Hex
layer4 = binascii.hexlify(layer3.encode()).decode()

with open("intercept.txt", "w") as f:
    f.write(layer4)

print(f"Final Hex: {layer4}")
