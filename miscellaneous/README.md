# Operation Black Vault — CTF Miscellaneous Series

<p align="center">
  <img src="https://img.shields.io/badge/Challenges-6-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python%2FC-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Deployment-Docker-2496ED?style=for-the-badge&logo=docker">
  <img src="https://img.shields.io/badge/Theme-COD%20Military-black?style=for-the-badge">
</p>

---

## Overview

**Operation Black Vault** is a military-themed (Call of Duty aesthetic) miscellaneous CTF series featuring 6 independent challenges spanning 3 difficulty tiers. These challenges blend forensic analysis, cryptography, steganography, polyglots, and esoteric programming into bizarre and complex problems.

All challenges run under the theme of a covert intelligence operation — "the Black Vault" — where agents must solve out-of-the-box puzzles to extract classified mission data.

---

## Challenge Map

| # | Codename | Category/Concept | Difficulty | Port | Flag |
|---|----------|------------------|------------|------|------|
| 01 | 🕵️ The Decoy | Git Forensics & History | 🟢 Easy | N/A | `BVAULT{g1t_r3fl0g_n3v3r_f0rg3t5}` |
| 02 | 🧩 Polyglot Paradox | Triple Polyglot (PDF/ZIP/PY) | 🟡 Medium | N/A | `BVAULT{p0lygl0t_m4d3_34sy_w1th_3x1f}` |
| 03 | ⏱️ The Chronos Anomaly | Network Timing Steganography | 🟡 Medium | N/A | `BVAULT{t1m1ng_15_3v3ryth1ng_1n_th3_v01d}` |
| 04 | 💻 Terminal Echo | Extreme Python PyJail (PEP 3131) | 🔴 Hard | 9004 | `BVAULT{n0_l3tt3r5_n0_pr0bl3m_un1c0d3_m4g1c}` |
| 05 | 📦 Schrödinger's Sandbox | C Compiler Sandbox / Shellcode | 🔴 Hard | 9005 | `BVAULT{1nl1n3_4553mbly_5y5c4ll_m4573r}` |
| 06 | 🕳️ The Infinite Void | Zero-Width Character Stego | 🟡 Medium | N/A | `BVAULT{z3r0_w1dth_ch4r4ct3r5_4r3_1nv151bl3}` |

---

## Project Structure

```
miscellaneous/
├── challenge-01-the-decoy/
│   ├── repo.zip                  # The challenge file
│   ├── description.txt
│   ├── README.md
│   ├── test_exploit.sh
│   └── writeup.md
│
├── challenge-02-polyglot-paradox/
│   ├── classified_document.pdf                     # The challenge file
│   ├── description.txt
│   ├── README.md
│   ├── test_exploit.py
│   └── writeup.md
│
├── challenge-03-the-chronos-classified_document.pdf/
│   ├── capture.pcap                # The challenge file
│   ├── description.txt
│   ├── README.md
│   ├── test_exploit.py
│   └── writeup.md
│
├── challenge-04-terminal-echo/
│   ├── Dockerfile                  # Server infrastructure
│   ├── flag.txt
│   ├── jail.py
│   ├── description.txt
│   ├── README.md
│   ├── test_exploit.py
│   └── writeup.md
│
├── challenge-05-schrodingers-sandbox/
│   ├── Dockerfile                  # Server infrastructure
│   ├── flag
│   ├── jail.py
│   ├── description.txt
│   ├── README.md
│   ├── test_exploit.py
│   └── writeup.md
│
└── challenge-06-the-infinite-void/
    ├── void.txt                    # The challenge file
    ├── build_void.py
    ├── description.txt
    ├── README.md
    ├── solve_void.py
    └── writeup.md
```

---

## Quick Start

### Local Testing (Docker)

Challenges 04 and 05 require Docker.

```bash
# Challenge 04
cd challenge-04-terminal-echo
docker build -t obv-ch04 .
docker run -d -p 9004:9004 obv-ch04

# Challenge 05
cd ../challenge-05-schrodingers-sandbox
docker build -t obv-ch05 .
docker run -d -p 9005:9005 obv-ch05
```

### Static Files
For challenges 01, 02, 03, and 06, simply provide the respective challenge files to the players. No server deployment is needed.

---

## Flag Format

All flags use the format: `BVAULT{...}`

---

## Challenge Writeups

Each challenge directory contains a complete `writeup.md` with:
- Vulnerability analysis (code-level)
- Step-by-step exploit walkthrough
- Python/Bash exploit scripts

---

*"The Black Vault does not officially exist. Neither do you. — PHANTOM Command"*
