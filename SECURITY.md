# Security Policy — Operation Black Vault CTF

## ⚠️ Intentional Vulnerabilities Disclaimer

This repository contains **intentionally vulnerable** software including:

- ELF binaries with stack overflows, format string bugs, heap corruption, and ROP gadgets
- Web applications with IDOR, SQLi, SSTI, JWT forgery, SSRF, and race condition vulnerabilities
- Python scripts demonstrating weak cryptography (small RSA exponents, LCG key streams, etc.)
- Forensic artifacts containing hidden data and malware simulation

**These vulnerabilities are by design.** They exist purely for educational and Capture The Flag training purposes. Do NOT deploy challenge services in production environments or on publicly accessible infrastructure without proper isolation.

---

## Scope

### ✅ In Scope (Please Report)

The following would constitute **unintended** security issues — things that go beyond the challenge design:

| Issue | Example |
|-------|---------|
| Credentials leaked in source code | Real API keys, passwords committed to the repo |
| CTFd platform configuration exposing real user PII | Admin credentials in config files |
| A challenge binary that allows arbitrary code execution **on the host** (not just the container) | Container escape |
| Incorrect flag validation allowing trivial bypass | Flag check always returns True |
| Challenge writeup accidentally published publicly before event end | `writeup.md` visible in public repo during live event |

### ❌ Out of Scope (Expected Behavior)

The following are **intentional** and should NOT be reported as vulnerabilities:

- Buffer overflows, format string bugs, or heap exploits in challenge ELF binaries
- SQL injection, IDOR, SSTI, JWT forgery in web challenge applications
- Weak RSA parameters, predictable PRNGs, or reused XOR keys in crypto challenges
- Hidden data in forensic artifacts (steganography, disk images, PCAPs)
- Anti-debugging techniques or obfuscation in reverse engineering binaries

---

## Reporting an Unintended Vulnerability

If you discover a genuine security issue (outside the challenge design) in this repository or its infrastructure:

1. **Do NOT open a public GitHub Issue** — this could expose the vulnerability before it's fixed.
2. **Email the maintainers directly** at the contact listed in the repository profile, or
3. **Use GitHub's Private Vulnerability Reporting** feature:
   - Go to the **Security** tab of this repository
   - Click **"Report a vulnerability"**
   - Provide a clear description, steps to reproduce, and potential impact

We aim to respond to all security reports within **48 hours** and resolve critical issues within **7 days**.

---

## Responsible Disclosure Policy

We follow a **coordinated disclosure** model:

- Reporters are asked to give us reasonable time to patch before public disclosure
- We will credit reporters in the `CHANGELOG.md` (unless they prefer anonymity)
- We do not pursue legal action against good-faith security researchers

---

## Supported Versions

| Version / Event | Supported |
|-----------------|-----------|
| OBV CTF 2026 (current) | ✅ Active |
| Future iterations | ✅ Will be supported |
| Past archived events | ⚠️ Best-effort only |
