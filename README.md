# Operation Black Vault (OBV) CTF Suite

Welcome to the **Operation Black Vault** Capture The Flag (CTF) challenge suite! This repository contains a complete, ready-to-deploy, military/tactical-themed CTF competition consisting of six distinct categories and 36 highly polished challenges. 

This environment is designed with a dark, psychological horror and espionage narrative, intended to test players in real-world offensive and defensive cybersecurity disciplines.

---

## 📂 Repository Structure

The CTF is split into six primary categories. Each category contains 6 challenges, scaling in difficulty from Easy to Hard.

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

### 5. [Reverse Engineering](./reverse_engineering/README.md)
Focuses on disassembling and decompiling stripped binaries, understanding custom VM architectures, bypassing anti-debugging techniques, and reversing malware algorithms.
* **Format:** ELF binaries (C/C++) requiring static and dynamic analysis.

### 6. [Miscellaneous](./miscellaneous/README.md)
Focuses on blending forensic analysis, cryptography, steganography, polyglots, and esoteric programming into bizarre and complex problems.
* **Format:** A mix of Python PyJails, C compiler sandboxes, polyglot files, and esoteric steganography.

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

### Static Challenges (Crypto, Forensics, Local Pwn, Misc)
These challenges only require the players to be provided with the target files. Inside each challenge directory, you will find:
* A `description.txt` meant for the players.
* The challenge files (e.g., `.elf`, `.pcap`, `.py`, `.txt`).
* A `writeup.md` file (FOR ORGANIZERS ONLY) detailing exactly how to solve the challenge.

---

## 📖 Organizer / Admin Manuals

For detailed instructions on running each category, refer to the organizer readmes located inside the category folders:
- **Forensics Organizer Manual:** `digital_forensics/ORGANIZER_MANUAL.md`
- **Web Exploitation Manual:** `web_exploitation/README.md`
- **Miscellaneous Manual:** `miscellaneous/README.md`
