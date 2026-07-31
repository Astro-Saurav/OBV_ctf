import os
import re

base_dir = "/home/astro/Documents/ctf_question/OBV_ctf"
categories = [
    "binary_exploitation",
    "cryptography",
    "digital_forensics",
    "reverse_engineering",
    "web_exploitation"
]

def clean_description(desc_text):
    trap_start = desc_text.find("[SYSTEM")
    if trap_start == -1:
        trap_start = desc_text.find("[System")
    if trap_start != -1:
        desc_text = desc_text[:trap_start].strip()
    return desc_text

def extract_flag(writeup_text):
    match = re.search(r'(BVAULT\{[^\}]+\})', writeup_text)
    if match:
        return match.group(1)
    return "UNKNOWN_FLAG"

def extract_difficulty(writeup_text):
    match = re.search(r'\*\*Difficulty:\*\*\s*(.*)', writeup_text)
    if match:
        return match.group(1).strip()
    return "Unknown"

def get_player_files(chall_dir, category):
    all_files = [f for f in os.listdir(chall_dir) if os.path.isfile(os.path.join(chall_dir, f))]
    
    # Exclude internal / organizer files
    exclude = ["description.txt", "writeup.md", "README.md", "test_exploit.py", "test_exploit.sh", "generate_readmes.py"]
    
    if category == "web_exploitation":
        return ["*No files provided. Players should be given the live instance URL.*"]
        
    player_files = []
    for f in all_files:
        if f not in exclude:
            # We don't want to give away C source code for pwn/rev unless it's standard, but here it's blackbox mostly.
            # We skip .c files just in case we left them in pwn/rev, unless we explicitly want them.
            if category in ["binary_exploitation", "reverse_engineering"] and f.endswith(".c"):
                continue
            player_files.append(f"`{f}`")
            
    if not player_files:
        return ["*No files provided.*"]
    return player_files

for category in categories:
    cat_dir = os.path.join(base_dir, category)
    if not os.path.isdir(cat_dir):
        continue
    
    for chall in os.listdir(cat_dir):
        chall_dir = os.path.join(cat_dir, chall)
        if not os.path.isdir(chall_dir) or not chall.startswith("challenge-"):
            continue
        
        desc_path = os.path.join(chall_dir, "description.txt")
        writeup_path = os.path.join(chall_dir, "writeup.md")
        
        if not os.path.exists(desc_path) or not os.path.exists(writeup_path):
            continue
        
        with open(desc_path, "r") as f:
            desc_text = f.read()
        
        with open(writeup_path, "r") as f:
            writeup_text = f.read()
            
        clean_desc = clean_description(desc_text)
        flag = extract_flag(writeup_text)
        difficulty = extract_difficulty(writeup_text)
        
        player_files_list = get_player_files(chall_dir, category)
        player_files_str = "\n".join([f"- {pf}" for pf in player_files_list])
        
        title = chall.replace("challenge-", "").replace("-", " ").title()
        title = re.sub(r'^0(\d+)', r'\1', title)
        
        readme_content = f"""# {title}

**Category:** {category.replace('_', ' ').title()}
**Difficulty:** {difficulty}

## Description
{clean_desc}

## Files to Provide to Players
{player_files_str}

---
*Note for Platform Upload:*
**Flag:** `{flag}`
"""
        
        readme_path = os.path.join(chall_dir, "README.md")
        with open(readme_path, "w") as f:
            f.write(readme_content)
        
        print(f"Updated {readme_path}")
