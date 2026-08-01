# Challenge 07: Shadow Architect
## Overview
- **Category:** Hybrid (OSINT / Forensics / Reverse / Web / Pwn)
- **Difficulty:** Hardcore (JEE Advanced Level)
- **Points:** 850
- **Author:** Phantom Command

## Summary
A rogue APT group ("Vanguard-9") left behind a memory dump, a C2 binary, and a network capture. Investigators must repair heap corruption, unflatten binary control flows, perform geospatial OSINT and wireless positioning, compute dynamic HMAC-TOTP keys, and execute a remote libc-leak ROP exploit against an internal web-connected service.

## Files Provided
- `files/core.dmp` — Corrupted heap memory dump containing metadata.
- `files/agent_v2` — Striped 64-bit ELF with Control Flow Flattening.
- `files/traffic.pcap` — Captured C2 handshake packets.

## Flag
`FLAG{Sh4d0w_4rch1t3ct_0s1nt_pwn_m4st3r_2026}`
