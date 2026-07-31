# Operation Black Vault (OBV) CTF Suite

Welcome to the **Operation Black Vault** Capture The Flag (CTF) challenge suite! This repository contains a complete, ready-to-deploy, military/tactical-themed CTF competition consisting of four distinct categories and 24 highly polished challenges. 

This environment is designed with a dark, psychological horror and espionage narrative, intended to test players in real-world offensive and defensive cybersecurity disciplines.

---

## 📂 Repository Structure

The CTF is split into four primary categories. Each category contains 6 challenges, scaling in difficulty from Easy to Hard.

### 1. [Binary Exploitation (Pwn)](./binary_exploitation/README.md)
Focuses on memory corruption, bypassing modern mitigations (NX, PIE, ASLR), Return-Oriented Programming (ROP), and heap exploitation.
* **Format:** ELF binaries (C/C++) running natively or in Dockerized `socat` wrappers.

### 2. [Web Exploitation](./web_exploitation/README.md)
Focuses on modern web application vulnerabilities, including IDOR, SQL Injection, JWT Forgery (`alg:none`), Server-Side Template Injection (SSTI), SSRF, and Race Conditions.
* **Format:** Containerized Go/HTML applications with built-in anti-AI/bot traps.

### 3. [Cryptography](./cryptography/README.md)
Focuses on subverting encryption protocols and mathematics, including base encoding, Vigenère ciphers, XOR masking, Hybrid Crypto, RSA (small `e` and Wiener's Attack), LCG key streams, and Mersenne Twister PRNG cracking.
* **Format:** Python scripts and encrypted ciphertext/public keys.

### 4. [Digital Forensics](./digital_forensics/ORGANIZER_MANUAL.md)
Focuses on uncovering hidden data, including DTMF audio decoding, PDF steganography, corrupted partition tables/disk images, PCAP network traffic analysis (USB/Network), and DNS Exfiltration malware.
* **Format:** Standalone artifacts (PCAPs, PDFs, Disk Images, Audio files). Includes psychological horror/jump scares.

---

## 🚩 Flag Format
All flags across the entire CTF follow the standard format:
`BVAULT{...}`

---

## 🛠️ Deploying the Challenges

### Web Exploitation & Networked Pwn
Challenges that require live network interaction (like Web Exploitation) are completely Dockerized for instant, consistent deployment.

1. Navigate to the specific challenge folder (e.g., `web_exploitation`).
2. Run `docker-compose up -d --build` (or the respective deployment script) to spin up the isolated challenge instances.
3. Challenges will be mapped to local host ports (e.g., `8001` through `8006`).

### Static Challenges (Crypto, Forensics, Local Pwn)
These challenges only require the players to be provided with the target files. Inside each challenge directory, you will find:
* A `description.txt` meant for the players.
* The challenge files (e.g., `.elf`, `.pcap`, `.py`, `.txt`).
* A `writeup.md` file (FOR ORGANIZERS ONLY) detailing exactly how to solve the challenge.

---

## 📖 Organizer / Admin Manuals

For detailed instructions on running each category, refer to the organizer readmes located inside the category folders:
- **Forensics Organizer Manual:** `digital_forensics/ORGANIZER_MANUAL.md`
- **Web Exploitation Manual:** `web_exploitation/README.md`
- **Binary Exploitation Manual:** `binary_exploitation/README.md`

> ⚠️ **IMPORTANT:** Do not deploy the `writeup.md`, `test_exploit.py`, or `ORGANIZER_MANUAL.md` files to the players! These contain the direct solutions and flags to the challenges.

---

## ✅ Quality Assurance & Anti-AI
- **100% Solvable:** Every single challenge has been dynamically verified via automated end-to-end exploit scripts.
- **Anti-AI Traps:** The web challenges include invisible honey-tokens and deceptive prompt injection vectors intended to actively mislead Large Language Models (LLMs) used by players to cheat, ensuring human intuition is required to succeed.
