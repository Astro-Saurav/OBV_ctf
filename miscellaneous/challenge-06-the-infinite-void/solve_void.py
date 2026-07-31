def decode_flag(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    binary = ""
    for c in content:
        if c == '\u200B':
            binary += '0'
        elif c == '\u200C':
            binary += '1'
            
    if not binary:
        print("No hidden binary found.")
        return
        
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    flag = "".join(chars)
    print("Extracted flag:", flag)

if __name__ == "__main__":
    decode_flag("void.txt")
