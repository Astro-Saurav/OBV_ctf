#!/usr/bin/env python3
import sys
import os
import subprocess
import tempfile
import string

def main():
    print("========================================")
    print("||     SCHRÖDINGER'S SANDBOX          ||")
    print("========================================")
    print("Please submit your C code to be compiled and executed.")
    print("End your submission with 'EOF' on a new line.")
    print("WARNING: Strings, includes, and system calls are strictly filtered.")
    
    code = ""
    while True:
        try:
            line = input()
            if line.strip() == "EOF":
                break
            code += line + "\n"
        except EOFError:
            break

    if len(code) > 2000:
        print("Code too long.")
        sys.exit(1)

    # The filter blocks
    banned = ['#include', 'main', 'system', 'exec', '"', "'", 'flag', 'open', 'read', 'write', 'syscall', 'int 0x80']
    for b in banned:
        if b in code.lower():
            print(f"ACCESS DENIED: Illegal keyword/character detected: {b}")
            sys.exit(1)

    # Wrap the code in a main function
    full_code = f"""
int main() {{
{code}
    return 0;
}}
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        src_path = os.path.join(tmpdir, "sandbox.c")
        bin_path = os.path.join(tmpdir, "sandbox")
        
        with open(src_path, "w") as f:
            f.write(full_code)
            
        # Compile
        compile_cmd = ["gcc", src_path, "-o", bin_path, "-w"]
        proc = subprocess.run(compile_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode != 0:
            print("Compilation failed.")
            sys.exit(1)
            
        print("Compilation successful. Executing...\n")
        
        # Execute
        try:
            exec_proc = subprocess.run([bin_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=2)
            print(exec_proc.stdout.decode('utf-8', errors='ignore'))
        except subprocess.TimeoutExpired:
            print("Execution timed out.")

if __name__ == "__main__":
    main()
