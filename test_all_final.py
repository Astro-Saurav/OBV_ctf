import os
import re
import subprocess

base = "/home/astro/Documents/ctf_question/OBV_ctf"
categories = [
    "binary_exploitation",
    "cryptography",
    "digital_forensics",
    "web_exploitation"
]

def extract_and_run(writeup_path, chal_dir, cat):
    with open(writeup_path, "r") as f:
        content = f.read()
    
    # Extract all blocks
    blocks = re.findall(r'```(python|bash)\n(.*?)```', content, re.DOTALL)
    if not blocks:
        return "NO_SCRIPT"
        
    script = ""
    lang = ""
    
    for b_lang, b_code in blocks:
        if "$ ./" in b_code or "$ strace" in b_code or "$ cp " in b_code:
            continue
        if "curl " in b_code or "binwalk " in b_code or "pwntools" in content or "from scapy" in b_code or "import " in b_code or "import requests" in b_code:
            script = b_code
            lang = b_lang
            break
            
    if not script:
        lang, script = blocks[-1]
    
    # Simple replace for Web Exploitation
    if cat == "web_exploitation":
        script = script.replace("<TARGET>", "localhost")
        script = script.replace("$TARGET", "http://localhost")
        
    is_bash = (lang == "bash" or "curl " in script or "binwalk " in script)
    if "pwntools" in content or "pwntools" in script.lower():
        is_bash = False

    if "N = ..." in script:
        script = script.replace("N = ...", "").replace("e = ...", "").replace("c = ...", "")
        file_to_parse = "public.txt" if ("public.txt" in script or "weak-rsa" in writeup_path) else "key.txt"
        parser_logic = f"""
with open('{file_to_parse}', 'r') as f:
    lines = f.readlines()
    N = int(lines[0].split('=')[1].strip())
    e = int(lines[1].split('=')[1].strip())
    c = int(lines[2].split('=')[1].strip())
"""
        script = parser_logic + script
        
    if is_bash:
        test_path = os.path.join(chal_dir, "test_exploit.sh")
        with open(test_path, "w") as f:
            f.write(script)
        cmd = ["bash", "test_exploit.sh"]
    else:
        test_path = os.path.join(chal_dir, "test_exploit.py")
        with open(test_path, "w") as f:
            f.write(script)
        cmd = ["/tmp/pwntools_venv/bin/python", "test_exploit.py"]
        
    try:
        out = subprocess.check_output(cmd, cwd=chal_dir, stderr=subprocess.STDOUT, timeout=20)
        output_str = out.decode()
        if "BVAULT{" in output_str:
            return f"SUCCESS: {output_str.strip()}"
        else:
            return f"FAIL (No flag outputted):\n{output_str}"
    except subprocess.CalledProcessError as e:
        return f"ERROR (Crash):\n{e.output.decode()}"
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

for cat in categories:
    print(f"=== Testing Category: {cat.upper()} ===")
    cat_dir = os.path.join(base, cat)
    if not os.path.exists(cat_dir): continue
    challenges = sorted([d for d in os.listdir(cat_dir) if "challenge-" in d])
    
    for chal in challenges:
        chal_dir = os.path.join(cat_dir, chal)
        writeup_path = os.path.join(chal_dir, "writeup.md")
        if not os.path.exists(writeup_path): continue
        res = extract_and_run(writeup_path, chal_dir, cat)
        if res.startswith("SUCCESS"):
            flag_match = re.search(r'BVAULT\{.*?\}', res)
            flag = flag_match.group(0) if flag_match else "UNKNOWN"
            print(f"[+] {chal}: PASS ({flag})")
        else:
            print(f"[!] {chal}: FAIL\n{res.split(chr(10))[0]}\n")

