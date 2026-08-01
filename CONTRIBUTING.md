# Contributing to Operation Black Vault CTF

Thank you for your interest in contributing to the **Operation Black Vault (OBV) CTF** challenge suite! This document outlines the standards and workflow for adding new challenges, fixing bugs, or improving existing content.

---

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Challenge Structure](#challenge-structure)
- [Naming Conventions](#naming-conventions)
- [Required Files Per Challenge](#required-files-per-challenge)
- [Flag Format](#flag-format)
- [Difficulty & Points Scale](#difficulty--points-scale)
- [Submission Workflow](#submission-workflow)
- [Code Style](#code-style)
- [What NOT to Contribute](#what-not-to-contribute)

---

## Getting Started

1. **Fork** the repository and clone your fork locally.
2. Create a new branch: `git checkout -b feat/challenge-name`
3. Install dependencies: `pip install -r requirements.txt`
4. Build your challenge following the structure below.
5. Test it locally and verify the flag works.
6. Open a Pull Request against `main`.

---

## Challenge Structure

Each challenge lives in its own subdirectory under the relevant category folder:

```
<category>/
└── challenge-<NN>-<kebab-case-name>/
    ├── README.md          # Player-facing challenge description
    ├── description.txt    # Raw text used in CTFd platform
    ├── writeup.md         # Organizer-only solution walkthrough
    ├── <challenge files>  # Binaries, scripts, pcaps, etc.
    └── test_exploit.*     # Automated solve script (py or sh)
```

For **web challenges**, additionally include:
```
    ├── Dockerfile
    ├── go.mod / requirements.txt
    ├── main.go / app.py
    └── templates/
```

For **challenges with downloadable files**, package them:
```
    ├── file/              # Unzipped challenge files
    └── file.zip           # Zipped version for distribution
```

---

## Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| Category folder | `snake_case` | `binary_exploitation/` |
| Challenge folder | `challenge-NN-kebab-name` | `challenge-07-rop-chain/` |
| Challenge number | Two-digit zero-padded | `07`, `10` |
| ELF binaries | `descriptive_name.elf` | `node_auth.elf` |
| Python scripts | `snake_case.py` | `encrypt.py`, `test_exploit.py` |
| Solve scripts | `test_exploit.py` or `test_exploit.sh` | — |

---

## Required Files Per Challenge

Every challenge **must** include these files before a PR will be accepted:

| File | Required | Description |
|------|----------|-------------|
| `README.md` | ✅ Yes | Player-facing description with story, objective, files list |
| `description.txt` | ✅ Yes | Plain-text CTFd platform description |
| `writeup.md` | ✅ Yes | Full organizer solution with step-by-step explanation |
| `test_exploit.py/.sh` | ✅ Yes | Automated solve script that outputs the flag |
| Challenge artifacts | ✅ Yes | The actual files players interact with |

### README.md Template

```markdown
# Challenge NN: [Challenge Name]

## Metadata
| Field       | Value        |
|-------------|--------------|
| Difficulty  | 🟢 Easy      |
| Category    | Cryptography |
| Points      | 200          |
| Flag Format | `BVAULT{...}` |

## Story
*"..."*

## Files Provided
- `file.zip` — challenge files archive

## Objective
...
```

---

## Flag Format

All flags **must** follow this exact format:

```
BVAULT{<meaningful_content>}
```

- Content should be thematically relevant to the challenge
- Avoid trivially guessable flags like `BVAULT{flag}` or `BVAULT{test}`
- Example: `BVAULT{r3turn_of_the_buffer_ov3rflow}`

---

## Difficulty & Points Scale

| Tier | Emoji | Points | Description |
|------|-------|--------|-------------|
| Easy | 🟢 | 100–300 | Single, well-known technique |
| Medium | 🟡 | 400–700 | Requires chaining 2–3 concepts |
| Hard | 🔴 | 800–1500 | Multi-step, novel or obscure techniques |
| Insane | ⚫ | 1500+ | Research-level, minimal hints |

---

## Submission Workflow

1. Open a **Pull Request** with the title: `[Category] Add Challenge NN: <Name>`
2. Fill in the PR template checklist
3. Ensure `test_exploit.*` outputs the correct flag automatically
4. A reviewer will verify the challenge is solvable and the writeup is accurate
5. Challenges are merged after at least **1 approval**

---

## Code Style

- **Python:** Follow PEP 8. Use type hints where appropriate.
- **Go (web):** Use `gofmt` formatting.
- **Shell scripts:** Use `#!/bin/bash` shebang. Quote all variables.
- **Docker:** Use small base images (`alpine`, `debian:slim`).

---

## What NOT to Contribute

- ❌ Real malware or actual exploits targeting production systems
- ❌ Challenges with flags that are impossible to solve without guessing
- ❌ Plagiarized challenges from other CTFs without attribution
- ❌ Challenges requiring paid tools or licensed software to solve
- ❌ Any content that violates the [Code of Conduct](CODE_OF_CONDUCT.md)

---

## Questions?

Open a [GitHub Issue](../../issues) or reach out to the maintainers. We're happy to help you craft a great challenge!
