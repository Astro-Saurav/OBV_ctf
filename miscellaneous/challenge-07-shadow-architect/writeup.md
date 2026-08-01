# Challenge Writeup: Operation Black Vault — Shadow Architect

## Overview
This multi-stage challenge requires coordinating output across digital forensics, control-flow disassembly, geospatial OSINT, dynamic MFA seed generation, and remote ROP exploitation.

---

## Step-by-Step Solution

### Stage 1: Heap Forensics & Reverse Engineering
1. **Memory Dump Repair (`core.dmp`):**
   * Inspect the memory dump using GDB or Volatility.
   * Notice corrupted chunk headers in the heap segment (`0x00000000` size fields).
   * Fix the size fields using a hex editor (`xxd` or ImHex) based on surrounding chunk pointers to repair the heap traversal.
   * Extract the decrypted buffer:
     * **Target IP:** `192.168.100.45`
     * **PGP Key ID:** `0x9ABCDEF012345678`

2. **Control Flow De-flattening (`agent_v2`):**
   * The binary uses a dispatcher variable inside an infinite loop with a `switch-case` construct.
   * Use an IDAPython script or `angr` to trace basic block state transitions and reconstruct the CFG.
   * Uncover the hardcoded fallback communication string: `[hash].phantom-vault.net`.

---

### Stage 2: Advanced OSINT & Geolocation
1. **PGP Key Server Lookup:**
   * Search `keyserver.ubuntu.com` or `pgp.mit.edu` for `0x9ABCDEF012345678`.
   * Find user metadata pointing to developer handle `vanguard_dev9` and repository `github.com/vanguard_dev9/dotfiles`.

2. **Commit History & Image Analysis:**
   * Browse commits in `vanguard_dev9/dotfiles`. Inspect deleted/force-pushed commit histories.
   * Retrieve the removed background image `wallpaper.jpg`.
   * Extract EXIF data to locate latitude/longitude coordinates (`48.8584° N, 2.2945° E`).
   * Cross-reference coordinates on **Wigle.net** to identify the local Wi-Fi SSID and BSSID:
     * **BSSID:** `00:11:22:33:44:55`

---

### Stage 3: Dynamic OSINT TOTP Authentication
1. **Seed Computation:**
   * Compute the HMAC-SHA256 digest using:
     * **Key:** `00:11:22:33:44:55` (BSSID)
     * **Message:** `A1B2C3D4E5F67890123456789ABCDEF012345678` (PGP Fingerprint)
2. **Generate MFA Token:**
   * Use the resulting key as the seed for standard TOTP generation (30-second window).
   * Submit token to `http://192.168.100.45/api/mfa` to gain admin access.

---

### Stage 4: Remote Binary Exploitation (PWN)
1. **Diagnostic Service Inspection:**
   * Access the diagnostic ping tool running on port `1337`.
   * Trigger the diagnostic leak command to obtain the address of `system()` in `libc`.
   * Calculate the base address of `libc` and locate `pop rdi; ret` and `/bin/sh`.

2. **Payload Construction:**
   ```text
   [ 72 Bytes Padding ] + [ ret (alignment) ] + [ pop rdi; ret ] + [ ptr to /bin/sh ] + [ system() ]
