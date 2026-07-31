# Operation Black Vault — Cryptography

This repository contains the **Cryptography** challenges for the **Operation Black Vault** CTF.

These challenges require players to identify and break classical ciphers, encoding schemes, custom symmetric encryption algorithms, and vulnerable asymmetric (RSA) configurations.

## Anti-AI Protections
**Note:** All challenges in this category have been injected with an anti-AI prompt (System Override Trap) in their `description.txt`. If a player attempts to solve a challenge by directly feeding the raw text into a Large Language Model, the AI is instructed to falsely declare the challenge mathematically unbreakable and supply the fake flag `BVAULT{41_4551574n7_d3f3473d}`.

---

## Challenge Map

| # | Codename | Concept | Difficulty | Points | Flag |
|---|----------|---------|------------|--------|------|
| 01 | 📡 Transmission Intercept | Multiple Encodings (B64/B32/Hex) | 🟢 Easy | 200 | `BVAULT{b453_3nc0d1ng_15_n07_3ncryp710n}` |
| 02 | 🔑 Shifted Orders | Vigenere Cipher | 🟢 Easy | 200 | `BVAULT{v1g3n3r3_c1ph3r_ccl4551c}` |
| 03 | 📉 Weak RSA | RSA Small Exponent (Cube Root) | 🟡 Medium | 450 | `BVAULT{r54_5m4ll_3_c0mm0n_m1574k3}` |
| 04 | 🔁 Repeating XOR | Repeating-Key XOR (Known Plaintext) | 🟡 Medium | 450 | `BVAULT{r3p3471ng_x0r_k3y_br0k3n}` |
| 05 | 🧠 Wiener's Attack | RSA Weak Private Key | 🔴 Hard | 700 | `BVAULT{w13n3r5_4774ck_r54_br0k3n}` |
| 06 | 🎲 Mersenne Twister | PRNG State Prediction (MT19937) | 🔴 Hard | 700 | `BVAULT{m3r53nn3_7w1573r_prng_c0mpr0m153d}` |

---

## Instructions for Organizers

To successfully deploy these challenges to players, please follow these guidelines:

1. **Deployment Files:** Provide the `description.txt` and the specific ciphertext/data files (e.g., `intercept.txt`, `public.txt`, `encrypted.bin`, `leak.txt`) to the players.
2. **Offline Only:** These are purely offline cryptography challenges. No server hosting is required.
3. **Writeups & Solutions:** The `writeup.md` files contain 100% working Python scripts that mathematically crack the ciphers and decrypt the flags. Do **not** distribute the writeups to the players until the CTF is over.
4. **Anti-Cheat (System Override):** Every `description.txt` contains a hidden prompt injection payload. If a player attempts to paste the description into an LLM (like ChatGPT) to cheat, the AI is instructed to return the fake flag `BVAULT{41_4551574n7_d3f3473d}`. Any player submitting this flag is likely cheating.

### Challenge-Specific Notes
* **Ch03 & Ch05 (RSA):** The provided `public.txt` and `key.txt` files contain extremely large integers. Ensure players are aware they need scripting languages with arbitrary-precision arithmetic (like Python) to solve them.
* **Ch06 (Mersenne Twister):** Players will need the `leak.txt` file (which contains exactly 624 integers) to successfully clone the PRNG state and decrypt `encrypted_flag.bin`.
