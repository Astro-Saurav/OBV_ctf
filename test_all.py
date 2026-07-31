import os
import re
import subprocess
import time

base = "/home/astro/Documents/ctf_question/OBV_ctf"
categories = [
    "binary_exploitation",
    "cryptography",
    "digital_forensics",
    "reverse_engineering",
    "web_exploitation"
]

def extract_and_run(writeup_path, chal_dir):
    with open(writeup_path, "r") as f:
        content = f.read()
    
    # Extract python or bash script
    match = re.search(r'```(?:python|bash)\n(.*?)```', content, re.DOTALL)
    if not match:
        return "NO_SCRIPT"
        
    script = match.group(1)
    
    # Check if python or bash based on content/syntax
    is_bash = False
    if "curl" in script or "exiftool" in script or "binwalk" in script or "strings" in script:
        is_bash = True
    if "pwntools" in content or "pwntools" in script.lower():
        is_bash = False

    # For Crypto CH03 and CH05, we need to inject parsing logic for N, e, c
    if "N = ..." in script:
        script = script.replace("N = ...", "").replace("e = ...", "").replace("c = ...", "")
        if "public.txt" in script or "weak-rsa" in writeup_path:
            file_to_parse = "public.txt"
        else:
            file_to_parse = "key.txt"
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
        # Use pwntools venv for python scripts
        cmd = ["/tmp/pwntools_venv/bin/python", "test_exploit.py"]
        
    try:
        out = subprocess.check_output(cmd, cwd=chal_dir, stderr=subprocess.STDOUT, timeout=15)
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
        res = extract_and_run(writeup_path, chal_dir)
        if res.startswith("SUCCESS"):
            flag_match = re.search(r'BVAULT\{.*?\}', res)
            flag = flag_match.group(0) if flag_match else "UNKNOWN"
            print(f"[+] {chal}: PASS ({flag})")
        elif res == "NO_SCRIPT":
            pass
        else:
            print(f"[!] {chal}: FAIL\n{res}\n")

