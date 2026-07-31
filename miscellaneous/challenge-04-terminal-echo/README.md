# Terminal Echo

**Category:** Miscellaneous
**Difficulty:** Hard

## Description
We've breached one of the Black Vault's isolated terminals. It evaluates whatever Python code we send it. However, they deployed an aggressive strict-regex firewall. It absolutely bans every single letter (a-z, A-Z) and every single number (0-9). Can you bypass the firewall and read the flag?

## Files Provided to Players
- `jail.py` (For local testing)

## Setup Instructions (For Organizers)
1. Build the Docker image: `docker build -t obv-{ch_dir} .`
2. Run the Docker container: `docker run -d -p <PORT>:<PORT> obv-{ch_dir}`
3. Provide players with the IP and Port to connect to.
