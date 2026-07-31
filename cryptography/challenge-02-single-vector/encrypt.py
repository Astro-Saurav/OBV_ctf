import base64

flag = "BVAULT{x0r_m45k_4nd_5ub5717u710n_br0k3n}"

# Layer 1: Single-byte XOR
xor_key = 0x42
layer1 = bytes([ord(c) ^ xor_key for c in flag])

# Layer 2: Custom Substitution
plain = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}_"
cipher = b"QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm9876543210_}{"

substitution_table = bytes.maketrans(plain, cipher)
layer2 = layer1.translate(substitution_table)

# Layer 3: Base32
layer3 = base64.b32encode(layer2)

with open("encrypted_doc.bin", "wb") as f:
    f.write(layer3)

print("Encrypted file generated.")
