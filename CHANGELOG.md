# Changelog — Operation Black Vault CTF

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] — 2026-08-01 · OBV CTF Live Event 🎉

### Event Summary

| Metric | Value |
|--------|-------|
| 🏆 Event Name | Operation Black Vault (OBV) CTF |
| 📅 Date | 2026-08-01 |
| 🧑‍💻 Platform | CTFd |
| 👥 Registered Users | ~344 |
| 🏅 Registered Teams | ~141 |
| 🚩 Flag Format | `BVAULT{...}` |
| 🎯 Total Challenges | 36 |
| 📂 Categories | 6 |

### 🥇 Hall of Fame — Final Leaderboard

| Place | Team | Score |
|-------|------|-------|
| 🥇 1st | Binary Sharks | 35,400 pts |
| 🥈 2nd | DOSA | 34,300 pts |
| 🥉 3rd | Cyberguys | 34,300 pts |

> Full scoreboard: [`OBV/Operation Black Vault-scoreboard.csv`](OBV/Operation%20Black%20Vault-scoreboard.csv)

---

### Added — Challenge Suite

#### 🔓 Binary Exploitation (6 challenges)
- `challenge-01-stack-smash` — Stack buffer overflow, ret2win (🟢 Easy, 200 pts)
- `challenge-02-data-leak` — Format string vulnerability (🟢 Easy, 300 pts)
- `challenge-03-command-execution` — ret2libc / ret2plt (🟡 Medium, 500 pts)
- `challenge-04-restricted-control` — ROP chain with partial RELRO (🟡 Medium, 700 pts)
- `challenge-05-ghost-memory` — Heap exploitation (🔴 Hard, 1000 pts)
- `challenge-06-syslog-nightmare` — Format string + heap combo (🔴 Hard, 1200 pts)

#### 🔐 Cryptography (8 challenges)
- `challenge-01-transmission-intercept` — Base encoding / Caesar (🟢 Easy, 100 pts)
- `challenge-01-phantom-shift` — Vigenère cipher (🟢 Easy, 200 pts)
- `challenge-02-shifted-orders` — XOR masking (🟢 Easy, 200 pts)
- `challenge-02-single-vector` — Single-byte XOR brute force (🟡 Medium, 400 pts)
- `challenge-03-weak-rsa` — RSA small public exponent (e=3) (🟡 Medium, 500 pts)
- `challenge-03-fast-prime` — RSA weak prime generation (🟡 Medium, 600 pts)
- `challenge-04-repeating-xor` — Repeating-key XOR (Kasiski) (🟡 Medium, 600 pts)
- `challenge-04-predictable-future` — LCG keystream prediction (🔴 Hard, 900 pts)
- `challenge-05-wieners-attack` — RSA Wiener's Attack (🔴 Hard, 1000 pts)
- `challenge-06-mersenne-twister` — MT19937 PRNG state recovery (🔴 Hard, 1200 pts)

#### 🌐 Web Exploitation (6 challenges)
- `challenge-01-ghost-signal` — IDOR (🟢 Easy, 100 pts)
- `challenge-02-dead-drop` — SQL Injection (🟢 Easy, 200 pts)
- `challenge-03-cipher-nest` — JWT Forgery (alg:none) (🟡 Medium, 400 pts)
- `challenge-04-shadow-grid` — Server-Side Template Injection (SSTI) (🟡 Medium, 600 pts)
- `challenge-05-blackout-protocol` — Server-Side Request Forgery (SSRF) (🔴 Hard, 900 pts)
- `challenge-06-vault-zero` — Race Condition (🔴 Hard, 1200 pts)

#### 🔍 Digital Forensics (6 challenges)
- `challenge-01-the-caller` — DTMF audio decoding (🟢 Easy)
- `challenge-02-phantom-document` — PDF steganography (🟢 Easy)
- `challenge-03-cursed-disk` — Corrupted partition table / disk image (🟡 Medium)
- `challenge-04-ghost-in-the-wires` — PCAP network traffic analysis (🟡 Medium)
- `challenge-05-polymorphic-nightmare` — USB PCAP forensics (🔴 Hard)
- `challenge-06-schizophrenic-malware` — DNS exfiltration malware analysis (🔴 Hard)

#### ⚙️ Reverse Engineering (6 challenges)
- `challenge-01-terminal-access` — Stripped binary, basic reversing (🟢 Easy)
- `challenge-02-obfuscated-entry` — String obfuscation bypass (🟢 Easy)
- `challenge-03-tamper-proof` — Anti-debugging techniques (🟡 Medium)
- `challenge-04-serial-interface` — Custom serial protocol reversing (🟡 Medium)
- `challenge-05-the-ghost-vm` — Custom VM architecture (🔴 Hard)
- `challenge-06-deep-root` — Backdoor daemon analysis (🔴 Hard)

#### 🎲 Miscellaneous (6 challenges)
- `challenge-01-the-decoy` — Steganography + forensics (🟢 Easy)
- `challenge-02-polyglot-paradox` — Polyglot file exploitation (🟡 Medium)
- `challenge-03-the-chronos-anomaly` — Time-based challenge (🟡 Medium)
- `challenge-04-terminal-echo` — PyJail escape (🟡 Medium)
- `challenge-05-schrodingers-sandbox` — Sandbox bypass (🔴 Hard)
- `challenge-06-the-infinite-void` — Esoteric programming (🔴 Hard)

---

### Added — Repository Infrastructure
- CTFd export (`OBV/` folder) with scoreboard, teams, users CSVs and full backup ZIP
- Per-challenge `README.md`, `description.txt`, `writeup.md`, `test_exploit.*`
- Web challenge Dockerfiles and `docker-compose.yml`
- Category-level `README.md` files

---

## [Unreleased] — Future Plans

### Planned for OBV CTF 2027
- [ ] Add `challenge-07` to each category (Insane tier ⚫)
- [ ] Add GitHub Actions CI to auto-verify `test_exploit.*` scripts
- [ ] Add hints system documentation
- [ ] Create participant-facing scoreboard archive page
- [ ] Add ARM64 / Windows binary exploitation challenges
