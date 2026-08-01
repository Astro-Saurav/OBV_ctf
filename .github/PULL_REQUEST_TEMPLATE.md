## Pull Request — Operation Black Vault CTF

### PR Type

- [ ] 🆕 New Challenge
- [ ] 🐛 Bug Fix (broken challenge / wrong flag)
- [ ] 📝 Documentation Update
- [ ] 🔧 Infrastructure / Deployment Fix
- [ ] ♻️  Refactor / Improvement

---

### Challenge Info *(if adding a new challenge)*

| Field | Value |
|-------|-------|
| **Category** | *(e.g., cryptography)* |
| **Challenge Name** | *(e.g., challenge-07-quantum-noise)* |
| **Difficulty** | *(🟢 Easy / 🟡 Medium / 🔴 Hard / ⚫ Insane)* |
| **Points** | *(e.g., 800)* |
| **Vulnerability / Concept** | *(e.g., RSA Bleichenbacher's attack)* |

---

### Description

> Briefly describe what this PR adds or fixes.

---

### Checklist

#### Required Files
- [ ] `README.md` — Player-facing description with story, objective, file list
- [ ] `description.txt` — Plain-text CTFd platform description
- [ ] `writeup.md` — Full step-by-step organizer solution (**ORGANIZERS ONLY**)
- [ ] `test_exploit.py` or `test_exploit.sh` — Automated solve script that prints the flag

#### For Web Challenges
- [ ] `Dockerfile` — Challenge is fully containerized
- [ ] Challenge starts correctly with `docker compose up`
- [ ] No hardcoded host-specific paths or ports

#### For Binary Challenges
- [ ] ELF binary is included and executable (`chmod +x`)
- [ ] Correct compiler flags documented in `writeup.md`
- [ ] Binary tested on target architecture (x86_64 Linux)

#### Quality
- [ ] Flag follows the `BVAULT{...}` format
- [ ] `test_exploit.*` automatically outputs the correct flag (no manual steps)
- [ ] Challenge is solvable — I have personally solved it using only the provided files
- [ ] Difficulty and points are appropriate per the [scale in CONTRIBUTING.md](CONTRIBUTING.md#difficulty--points-scale)
- [ ] No real credentials, API keys, or sensitive data leaked in files

---

### Testing

> Describe how you tested this challenge. What environment did you use?

```
$ python3 test_exploit.py
[+] Flag: BVAULT{...}
```

---

### Screenshots / Recordings *(optional)*

> Add any relevant screenshots of the challenge working.
