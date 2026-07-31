# Operation Black Vault (OBV) CTF Suite

Welcome to the **Operation Black Vault CTF Suite**. This repository contains a collection of highly creative, incredibly difficult, and technically unique CTF (Capture The Flag) challenges, designed for advanced players who are looking for a true test of their skills.

## Categories

Currently, the repository features the **Miscellaneous** category.

### Miscellaneous

This category contains 6 challenges that blend forensic analysis, cryptography, steganography, polyglots, and esoteric programming into bizarre and complex problems.

1. **[The Decoy](miscellaneous/challenge-01-the-decoy)** - *Easy*
   - A forensic analysis challenge focusing on retrieving data from the hidden history and reflogs of a seemingly empty git repository.
2. **[Polyglot Paradox](miscellaneous/challenge-02-polyglot-paradox)** - *Medium*
   - A file format challenge featuring a triple-polyglot file that is simultaneously a valid PDF document, a ZIP archive, and an executable Python script.
3. **[The Chronos Anomaly](miscellaneous/challenge-03-the-chronos-anomaly)** - *Medium*
   - A network analysis challenge where the secret flag is not contained within the packets themselves, but encoded within the microsecond timing deltas between them.
4. **[Terminal Echo](miscellaneous/challenge-04-terminal-echo)** - *Hard*
   - An extreme Python PyJail challenge that implements a strict regex firewall completely banning all alphanumeric characters (no letters, no numbers), requiring Unicode normalization bypass techniques (PEP 3131).
5. **[Schrödinger's Sandbox](miscellaneous/challenge-05-schrodingers-sandbox)** - *Hard*
   - A C compiler sandbox challenge that bans all strings (no quotes) and standard I/O library calls. Exploitation requires injecting raw assembly shellcode using hex arrays and invoking `mprotect`.
6. **[The Infinite Void](miscellaneous/challenge-06-the-infinite-void)** - *Medium*
   - A steganography challenge that hides binary data entirely inside zero-width characters (invisible characters) embedded in an innocent-looking text file.

## Repository Structure

Each challenge has its own directory containing:
- `README.md` - Challenge description and setup instructions for organizers.
- The challenge files to be provided to players (e.g. `capture.pcap`, `repo.zip`, `void.txt`).
- `writeup.md` - The official solution writeup.
- Source code, build scripts, or Dockerfiles used to generate or host the challenge.

## Setup Instructions

Most challenges are static files that can simply be provided to the players. Challenges that require a server to run (such as `Terminal Echo` and `Schrödinger's Sandbox`) come with `Dockerfile`s. To deploy them:

```bash
cd miscellaneous/challenge-04-terminal-echo
docker build -t obv-ch04 .
docker run -d -p 9004:9004 obv-ch04
```

## Contributing

The challenges in this repository are designed to be "10/10" in creativity and difficulty. If you have an idea for a challenge that pushes the boundaries of traditional CTF formats, feel free to submit a pull request!
