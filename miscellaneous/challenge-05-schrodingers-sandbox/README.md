# Schrödinger's Sandbox

**Category:** Miscellaneous
**Difficulty:** Hard

## Description
We discovered a C compiler sandbox inside the Black Vault. It takes your C code, compiles it, and runs it on their server. However, they've completely restricted any string usage. You cannot use double quotes (`"`), single quotes (`'`), or include any header files (`#include`). They also specifically banned keywords like `system`, `exec`, `open`, `read`, `write`, `flag`, and `syscall`. Can you read `/home/ctf/flag` when you can't even type the word 'flag' or use strings?

## Files Provided to Players
- `jail.py` (For local testing)

## Setup Instructions (For Organizers)
1. Build the Docker image: `docker build -t obv-{ch_dir} .`
2. Run the Docker container: `docker run -d -p <PORT>:<PORT> obv-{ch_dir}`
3. Provide players with the IP and Port to connect to.
