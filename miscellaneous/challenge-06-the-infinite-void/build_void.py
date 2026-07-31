def encode_flag(flag, base_text):
    # Mapping
    # 0 -> Zero-width space (U+200B)
    # 1 -> Zero-width non-joiner (U+200C)
    
    binary = ''.join(format(ord(c), '08b') for c in flag)
    
    hidden_payload = ""
    for bit in binary:
        if bit == '0':
            hidden_payload += '\u200B'
        else:
            hidden_payload += '\u200C'
            
    # Inject it between the first and second characters of the base text
    result = base_text[0] + hidden_payload + base_text[1:]
    
    with open("void.txt", "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    flag = "BVAULT{z3r0_w1dth_ch4r4ct3r5_4r3_1nv151bl3}"
    text = "The void contains nothing. Do not stare too long."
    encode_flag(flag, text)
    print("void.txt generated.")
