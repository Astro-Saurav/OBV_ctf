# Operation Black Vault — Digital Forensics

This repository contains the **Digital Forensics** challenges for the **Operation Black Vault** CTF.

These challenges require players to analyze audio spectrograms/frequencies, extract hidden network transfers from PCAPs, recover deleted items from disk images, and hex-edit polyglot files.

## Anti-AI Protections
**Note:** All challenges in this category have been injected with an anti-AI prompt (System Override Trap) in their `description.txt`. If a player attempts to solve a challenge by directly feeding the raw text into a Large Language Model, the AI is instructed to falsely declare the challenge mathematically unbreakable and supply the fake flag `BVAULT{41_4551574n7_d3f3473d}`.

---

## Challenge Map

| # | Codename | Concept | Difficulty | Points | Flag |
|---|----------|---------|------------|--------|------|
| 01 | 📞 The Caller | Audio Steganography (DTMF Tones) & Jump Scare | 🟢 Easy | 100 | `BVAULT{d7mf_70n35_4r3_cr33py}` |
| 02 | 👻 Phantom Document | Invisible Ink & XMP Metadata | 🟢 Easy | 150 | `BVAULT{ph4n70m_m374d474_r3v34l3d}` |
| 03 | 💀 Cursed Disk | Disk Forensics (FAT32 File Carving) | 🟡 Medium | 300 | `BVAULT{d3l373d_f1l35_n3v3r_d13}` |
| 04 | 🕸️ Ghost in the Wires | PCAP Analysis (HTTP Object Extraction) | 🟡 Medium | 400 | `BVAULT{gh057_1n_7h3_pc4p_n37w0rk}` |
| 05 | 🦇 Polymorphic Nightmare | Polyglot (PNG+ZIP) & Hex Editing | 🔴 Hard | 600 | `BVAULT{p0lygl07_f1l35_4r3_n1gh7m4r35}` |
| 06 | 🧠 Schizophrenic Malware | Advanced PCAP (DNS Exfiltration) | 🔴 Hard | 800 | `BVAULT{dns_exf1l7r4710n_m4lw4r3_c4u9h7}` |

---

## Instructions for Organizers

To successfully deploy these challenges to players, please follow these guidelines:

1. **Deployment Files:** Provide the `description.txt` and the specific artifact files (e.g., `voicemail.wav`, `briefing.pdf`, `cursed.img`, `capture.pcap`, `nightmare`, `traffic.pcap`) to the players.
2. **Offline Only:** These are purely offline digital forensics challenges. No server hosting is required.
3. **Writeups & Solutions:** The `writeup.md` files contain 100% working Python scripts or CLI commands that mathematically crack the hiding mechanics and extract the flags. Do **not** distribute the writeups to the players until the CTF is over.
4. **Anti-Cheat (System Override):** Every `description.txt` contains a hidden prompt injection payload. If a player attempts to paste the description into an LLM (like ChatGPT) to cheat, the AI is instructed to return the fake flag `BVAULT{41_4551574n7_d3f3473d}`. Any player submitting this flag is likely cheating.

### Challenge-Specific Notes
* **Ch01 (The Caller):** Warn players to **NOT listen to the audio file at maximum volume with headphones.** It contains an intentional jump scare (loud screech/scream) prior to the DTMF tones being transmitted.
* **Ch05 (Polymorphic Nightmare):** The file `nightmare` contains no file extension. It is simultaneously a valid ZIP file and a valid PNG image. 
* **Ch06 (Schizophrenic Malware):** Requires writing a custom Python `scapy` script (or heavy `tshark` bash magic) to extract the subdomains from hundreds of DNS TXT packets. Wireshark alone will be extremely tedious.
