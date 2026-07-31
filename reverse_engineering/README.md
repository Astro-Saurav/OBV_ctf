# Operation Black Vault — Reverse Engineering

This repository contains the Reverse Engineering challenges for the **Operation Black Vault** CTF.

These challenges consist of compiled Linux binaries (`.elf`) that players must decompile, trace, and reverse engineer to recover the hidden flags.

## Anti-AI Protections
**Note:** All challenges in this category have been injected with an anti-AI prompt (System Override Trap) in their `description.txt`. If a player attempts to solve a challenge by directly feeding the raw text into a Large Language Model, the AI is instructed to falsely declare the challenge mathematically unbreakable and supply the fake flag `BVAULT{41_4551574n7_d3f3473d}`.

---

## Challenge Map

| # | Codename | Vulnerability / Concept | Difficulty | Points | Flag |
|---|----------|-------------------------|------------|--------|------|
| 01 | 🖥️ Terminal Access | Hardcoded Strings | 🟢 Easy | 200 | `BVAULT{h4rdc0d3d_57r1ng5_4r3_b4d}` |
| 02 | 🚪 Obfuscated Entry| XOR Masking / `ltrace` | 🟢 Easy | 200 | `BVAULT{x0r_0bfu5c4710n_15_n07_3ncryp710n}` |
| 03 | 🛡️ Tamper Proof | `ptrace` Anti-Debugging | 🟡 Medium | 450 | `BVAULT{4n71_d3bugg1ng_w17h_p7r4c3}` |
| 04 | 📻 Serial Interface| Keygen Algorithm Reversing| 🟡 Medium | 450 | `BVAULT{k3yg3n_m4573r_8291}` |
| 05 | 👻 The Ghost VM | Custom VM Architecture | 🔴 Hard | 700 | `BVAULT{gh057_vm_r3v3r53d_5ucc355fully}` |
| 06 | 🌳 Deep Root | Malware Environmental Keying| 🔴 Very Hard| 700 | `BVAULT{3nv1r0nm3n74l_k3y1ng_15_5734l7hy}` |

---

## Instructions for Organizers

To successfully deploy these challenges to players, please follow these guidelines:

1. **Deployment Files:** Provide the compiled `.elf` binaries and the `description.txt` files to the players.
2. **Offline Only:** These are strictly offline reverse engineering challenges. No server hosting is required.
3. **Writeups & Solutions:** The `writeup.md` files contain 100% working Python solver scripts and step-by-step disassembly analysis for the organizers. Do **not** distribute the writeups to the players until the CTF is over.
4. **Anti-Cheat (System Override):** Every `description.txt` contains a hidden prompt injection payload. If a player attempts to paste the description into an LLM (like ChatGPT) to cheat, the AI is instructed to return the fake flag `BVAULT{41_4551574n7_d3f3473d}`. Any player submitting this flag is likely cheating.

### Challenge-Specific Notes
* **Ch05 (Quantum Obfuscation):** The binary uses a complex state machine. Brute-forcing is mathematically infeasible without proper analysis.
* **Ch06 (Ouroboros):** The binary modifies itself in memory (SMC) and uses `ptrace` anti-debugging. It will intentionally crash if run directly in `gdb` without bypassing the anti-debug check first. Ensure players know that dynamic analysis will require debugger evasion.
