# Operation Black Vault (OBV) CTF Suite

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Challenges](https://img.shields.io/badge/Challenges-36-blueviolet)](#-repository-structure)
[![Categories](https://img.shields.io/badge/Categories-6-blue)](#-repository-structure)
[![Platform](https://img.shields.io/badge/Platform-CTFd-orange)](https://ctfd.io)
[![Flag Format](https://img.shields.io/badge/Flag%20Format-BVAULT%7B...%7D-red)](#-flag-format)
[![Participants](https://img.shields.io/badge/Participants-344-green)](OBV/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

</div>

<br/>

> *"The vault has been breached. The operation has begun. There is no turning back, Agent."*

Welcome to the **Operation Black Vault** Capture The Flag (CTF) challenge suite — a complete, ready-to-deploy, military/tactical-themed CTF competition with **36 challenges** across **6 categories**. Designed with a dark psychological horror and espionage narrative, it tests players in real-world offensive and defensive cybersecurity disciplines.

---

## ⚡ Quick Start

### For Participants

```bash
# 1. Clone the repo
git clone https://github.com/Astro-Saurav/OBV_ctf.git
cd OBV_ctf

# 2. Install Python tools
pip install -r requirements.txt

# 3. Navigate to your challenge
cd cryptography/challenge-01-phantom-shift/
cat description.txt        # Read the challenge
ls file/                   # Explore challenge files
python3 test_exploit.py    # Run the reference solve (after you've solved it!)
```

### For Organizers

```bash
# 1. Clone & setup everything (Python + Docker)
git clone https://github.com/Astro-Saurav/OBV_ctf.git
cd OBV_ctf
chmod +x setup.sh && ./setup.sh

# 2. Launch all web challenges
docker compose up -d --build

# 3. Verify all containers
docker compose ps
```

---

## 📂 Repository Structure

The CTF is organized into **6 categories**. Each challenge contains a player-facing `README.md`, a `description.txt` for CTFd, challenge artifacts, and an organizer-only `writeup.md`.

### 1. [🔓 Binary Exploitation (Pwn)](./binary_exploitation/README.md)
Focuses on memory corruption, bypassing modern mitigations (NX, PIE, ASLR), Return-Oriented Programming (ROP), and heap exploitation.
* **Format:** ELF binaries (C/C++) running natively or in Dockerized `socat` wrappers.
* **Organizer Docs:** [binary_exploitation/ORGANIZER_MANUAL.md](./binary_exploitation/ORGANIZER_MANUAL.md)

### 2. [🌐 Web Exploitation](./web_exploitation/README.md)
Focuses on modern web application vulnerabilities, including IDOR, SQL Injection, JWT Forgery (`alg:none`), Server-Side Template Injection (SSTI), SSRF, and Race Conditions.
* **Format:** Containerized Go/HTML applications with built-in anti-AI/bot traps.
* **Organizer Docs:** [web_exploitation/DEPLOYMENT.md](./web_exploitation/DEPLOYMENT.md)

### 3. [🔐 Cryptography](./cryptography/README.md)
Focuses on subverting encryption protocols and mathematics, including base encoding, Vigenère ciphers, XOR masking, Hybrid Crypto, RSA (small `e` and Wiener's Attack), LCG key streams, and Mersenne Twister PRNG cracking.
* **Format:** Python scripts and encrypted ciphertext/public keys.
* **Organizer Docs:** [cryptography/ORGANIZER_MANUAL.md](./cryptography/ORGANIZER_MANUAL.md)

### 4. [🔍 Digital Forensics](./digital_forensics/README.md)
Focuses on uncovering hidden data, including DTMF audio decoding, PDF steganography, corrupted partition tables/disk images, PCAP network traffic analysis (USB/Network), and DNS Exfiltration malware.
* **Format:** Standalone artifacts (PCAPs, PDFs, Disk Images, Audio files). Includes psychological horror/jump scares.
* **Organizer Docs:** [digital_forensics/ORGANIZER_MANUAL.md](./digital_forensics/ORGANIZER_MANUAL.md)

### 5. [⚙️ Reverse Engineering](./reverse_engineering/README.md)
Focuses on disassembling and decompiling stripped binaries, understanding custom VM architectures, bypassing anti-debugging techniques, and reversing malware algorithms.
* **Format:** ELF binaries (C/C++) requiring static and dynamic analysis.
* **Organizer Docs:** [reverse_engineering/ORGANIZER_MANUAL.md](./reverse_engineering/ORGANIZER_MANUAL.md)

### 6. [🎲 Miscellaneous](./miscellaneous/README.md)
Focuses on blending forensic analysis, cryptography, steganography, polyglots, and esoteric programming into bizarre and complex problems.
* **Format:** A mix of Python PyJails, C compiler sandboxes, polyglot files, and esoteric steganography.
* **Organizer Docs:** [miscellaneous/ORGANIZER_MANUAL.md](./miscellaneous/ORGANIZER_MANUAL.md)

---

## 🚩 Flag Format

All flags across the entire CTF follow the standard format:

```
BVAULT{...}
```

---

## 🏆 Hall of Fame — OBV CTF 2026

> Event held on **2026-08-01** · Platform: **CTFd** · Participants: **~344** · Teams: **~141**

| 🏅 Place | Team | Score |
|----------|------|-------|
| 🥇 1st | **Binary Sharks** | **35,400 pts** |
| 🥈 2nd | *(see scoreboard)* | — |
| 🥉 3rd | *(see scoreboard)* | — |

> 📊 Full scoreboard: [OBV/Operation Black Vault-scoreboard.csv](OBV/Operation%20Black%20Vault-scoreboard.csv)
> 📦 Full CTFd backup: [OBV/](OBV/)

---

## 🛠️ Deploying the Challenges

### Web Exploitation (Docker)

Challenges requiring live network interaction are fully Dockerized.

```bash
# From repo root — launches all 6 web challenges
docker compose up -d --build

# Check status
docker compose ps

# View logs
docker compose logs -f

# Tear down
docker compose down
```

| Challenge | URL | Vulnerability |
|-----------|-----|---------------|
| Ghost Signal | http://localhost:8001 | IDOR |
| Dead Drop | http://localhost:8002 | SQL Injection |
| Cipher Nest | http://localhost:8003 | JWT Forgery |
| Shadow Grid | http://localhost:8004 | SSTI |
| Blackout Protocol | http://localhost:8005 | SSRF |
| Vault Zero | http://localhost:8006 | Race Condition |

### Static Challenges (Crypto, Forensics, Pwn, Misc)

Provide the files in each `challenge-XX-*/` folder to players. Each contains:

| File | Audience | Purpose |
|------|----------|---------|
| `description.txt` | Players | CTFd challenge description |
| `README.md` | Players | Story, objective, file list |
| `file/` or artifacts | Players | The actual challenge files |
| `file.zip` | Players | Zipped version for download |
| `writeup.md` | **Organizers only** | Step-by-step solution |
| `test_exploit.*` | **Organizers only** | Automated solve verification |

---

## 📋 Prerequisites

| Tool | Required For | Install |
|------|-------------|---------|
| Python 3.10+ | Crypto, Misc, Pwn scripts | `apt install python3` |
| Docker + Compose | Web challenges | [docs.docker.com](https://docs.docker.com/get-docker/) |
| pwntools | Binary exploitation | `pip install pwntools` |
| Ghidra / radare2 | Reverse engineering | [ghidra-sre.org](https://ghidra-sre.org/) |
| Wireshark / tshark | Digital forensics | `apt install wireshark` |
| GDB + GEF | Binary exploitation | `apt install gdb` |

```bash
# Install all Python dependencies at once
pip install -r requirements.txt
```

---

## 📖 Organizer Manuals

| Category | Manual |
|----------|--------|
| 🔓 Binary Exploitation | [ORGANIZER_MANUAL.md](binary_exploitation/ORGANIZER_MANUAL.md) |
| 🌐 Web Exploitation | [DEPLOYMENT.md](web_exploitation/DEPLOYMENT.md) |
| 🔐 Cryptography | [ORGANIZER_MANUAL.md](cryptography/ORGANIZER_MANUAL.md) |
| 🔍 Digital Forensics | [ORGANIZER_MANUAL.md](digital_forensics/ORGANIZER_MANUAL.md) |
| ⚙️ Reverse Engineering | [ORGANIZER_MANUAL.md](reverse_engineering/ORGANIZER_MANUAL.md) |
| 🎲 Miscellaneous | [ORGANIZER_MANUAL.md](miscellaneous/ORGANIZER_MANUAL.md) |

---

## 🤝 Contributing

We welcome contributions — new challenges, bug fixes, and improvements!

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Challenge file structure and naming conventions
- Required files per challenge
- Difficulty & points scale
- PR submission workflow

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

> ⚠️ All challenge binaries and web apps are **intentionally vulnerable** for educational purposes only. Do not deploy on production infrastructure. See [SECURITY.md](SECURITY.md) for the full policy.

---

## 📄 Additional Documents

| Document | Purpose |
|----------|---------|
| [CHANGELOG.md](CHANGELOG.md) | Event history, challenge list, version log |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to add challenges and contribute |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community and competition rules |
| [SECURITY.md](SECURITY.md) | Vulnerability disclosure policy |
| [OBV/README.md](OBV/README.md) | Competition data & export documentation |

<br/>

<div align="center">
<sub>Built with ❤️ for the cybersecurity community · Operation Black Vault CTF 2026</sub>
</div>
