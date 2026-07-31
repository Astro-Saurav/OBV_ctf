import os

challenges = {
    "challenge-01-the-decoy": {
        "title": "The Decoy",
        "difficulty": "Easy",
        "description": "We found a suspicious git repository belonging to the Black Vault. They thought they deleted the sensitive data, but the internet never forgets. Can you find what they tried to hide?",
        "files_provided": ["`repo.zip` (The git repository)"]
    },
    "challenge-02-polyglot-paradox": {
        "title": "Polyglot Paradox",
        "difficulty": "Medium",
        "description": "This file was recovered from a breached Black Vault server. The file command says it's a PDF. Our analysts say it's a ZIP archive. Executing it runs a Python script. Can you unravel this triple-polyglot and find the hidden flag?",
        "files_provided": ["`classified_document.pdf`"]
    },
    "challenge-03-the-chronos-anomaly": {
        "title": "The Chronos Anomaly",
        "difficulty": "Medium",
        "description": "We intercepted some network traffic from a Black Vault operative. The packet contents look like random noise, but our timing analysis suggests otherwise. Is the operative communicating through the fabric of time itself?",
        "files_provided": ["`capture.pcap`"]
    },
    "challenge-04-terminal-echo": {
        "title": "Terminal Echo",
        "difficulty": "Hard",
        "description": "We've breached one of the Black Vault's isolated terminals. It evaluates whatever Python code we send it. However, they deployed an aggressive strict-regex firewall. It absolutely bans every single letter (a-z, A-Z) and every single number (0-9). Can you bypass the firewall and read the flag?",
        "files_provided": ["`jail.py` (For local testing)"]
    },
    "challenge-05-schrodingers-sandbox": {
        "title": "Schrödinger's Sandbox",
        "difficulty": "Hard",
        "description": "We discovered a C compiler sandbox inside the Black Vault. It takes your C code, compiles it, and runs it on their server. However, they've completely restricted any string usage. You cannot use double quotes (`\"`), single quotes (`'`), or include any header files (`#include`). They also specifically banned keywords like `system`, `exec`, `open`, `read`, `write`, `flag`, and `syscall`. Can you read `/home/ctf/flag` when you can't even type the word 'flag' or use strings?",
        "files_provided": ["`jail.py` (For local testing)"]
    },
    "challenge-06-the-infinite-void": {
        "title": "The Infinite Void",
        "difficulty": "Medium",
        "description": "\"The void contains nothing. Do not stare too long.\"\n\nWe found this strange text file floating around the vault servers. Our analysts claim there is a hidden message inside, but we can't see anything with our bare eyes. Can you look closer?",
        "files_provided": ["`void.txt`"]
    }
}

base_dir = "/home/astro/Documents/ctf_question/OBV_ctf/miscellaneous"

for ch_dir, info in challenges.items():
    readme_path = os.path.join(base_dir, ch_dir, "README.md")
    content = f"""# {info['title']}

**Category:** Miscellaneous
**Difficulty:** {info['difficulty']}

## Description
{info['description']}

## Files Provided to Players
"""
    for f in info['files_provided']:
        content += f"- {f}\n"
    
    content += "\n## Setup Instructions (For Organizers)\n"
    if "challenge-04" in ch_dir or "challenge-05" in ch_dir:
        content += "1. Build the Docker image: `docker build -t obv-{ch_dir} .`\n"
        content += "2. Run the Docker container: `docker run -d -p <PORT>:<PORT> obv-{ch_dir}`\n"
        content += "3. Provide players with the IP and Port to connect to.\n"
    else:
        content += "1. No server infrastructure required. Just provide the files to the players.\n"
        
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Challenge READMEs generated.")
