# Digital Forensics — Organizer Manual

> **FOR ORGANIZERS ONLY** — This document contains solutions, flag values, and artifact generation instructions. Do not share with participants.

---

## Category Overview

| Field | Value |
|-------|-------|
| **Total Challenges** | 6 |
| **Difficulty Range** | 🟢 Easy → 🔴 Hard |
| **Format** | Standalone artifacts (audio, PDF, disk image, PCAP) |
| **Flag Format** | `BVAULT{...}` |
| **Deployment** | Static files only (no server required) |
| **Special Note** | Challenges 05 & 06 contain psychological horror elements — warn participants |

---

## Prerequisites / Required Tools (Organizer)

```bash
# Forensics toolkit
sudo apt-get install -y \
  binwalk foremost exiftool steghide stegsolve \
  wireshark tshark volatility3 \
  testdisk photorec \
  sox ffmpeg dtmf2num \
  python3-pip

pip install dpkt scapy
```

---

## Challenge Reference

### Challenge 01 — The Caller 🟢 Easy

| Field | Value |
|-------|-------|
| **Files** | Audio file (`.wav`) |
| **Concept** | DTMF (Dual-Tone Multi-Frequency) audio decoding |
| **Flag** | `BVAULT{dtmf_c4ll_d3c0d3d}` |

**Solve summary:** Open the WAV file in Audacity or run through `multimon-ng`. The DTMF tones encode a phone number that maps to the flag via a provided legend.

**Decode command:**
```bash
multimon-ng -t wav -a DTMF <audio_file>.wav
# or
sox <audio_file>.wav -t raw -r 22050 -e signed -b 16 - | multimon-ng -t raw -a DTMF -
```

**Regenerate artifact:**
```bash
python3 -c "
# Generate DTMF tones that encode the flag digits
# (use sox or pydub with DTMF tone tables)
"
```

---

### Challenge 02 — Phantom Document 🟢 Easy

| Field | Value |
|-------|-------|
| **Files** | `classified.pdf` |
| **Concept** | PDF steganography — hidden layer / metadata extraction |
| **Flag** | `BVAULT{ph4nt0m_d0c_r3v34l3d}` |

**Solve summary:**
1. `exiftool classified.pdf` — check metadata
2. `strings classified.pdf | grep BVAULT` — flag hidden in stream
3. Or: `binwalk classified.pdf` — extract embedded file

**Verify:**
```bash
strings classified.pdf | grep -oP 'BVAULT\{[^}]+\}'
```

---

### Challenge 03 — Cursed Disk 🟡 Medium

| Field | Value |
|-------|-------|
| **Files** | `cursed.img` (disk image, ~50MB) |
| **Concept** | Corrupted partition table / MBR recovery |
| **Flag** | `BVAULT{p4rt1t10n_t4bl3_r3st0r3d}` |

**Solve summary:**
1. Mount the image: `sudo mount -o loop cursed.img /mnt/tmp`
2. If fails, use `testdisk cursed.img` to rebuild partition table
3. Recovered file system contains the flag file

**Verify:**
```bash
testdisk cursed.img
# Navigate: Analyse → Quick Search → List files → flag.txt
```

---

### Challenge 04 — Ghost in the Wires 🟡 Medium

| Field | Value |
|-------|-------|
| **Files** | `capture.pcap` |
| **Concept** | PCAP network traffic analysis — HTTP/DNS exfiltration |
| **Flag** | `BVAULT{n3tw0rk_tr4ff1c_d3c0d3d}` |

**Solve summary:**
1. Open in Wireshark
2. Filter: `http` — find POST request with encoded flag
3. Decode body: Base64 → flag

**tshark one-liner:**
```bash
tshark -r capture.pcap -T fields -e http.file_data 2>/dev/null \
  | base64 -d | grep BVAULT
```

---

### Challenge 05 — Polymorphic Nightmare 🔴 Hard

| Field | Value |
|-------|-------|
| **Files** | `usb_capture.pcap` |
| **Concept** | USB HID PCAP analysis — reconstruct keystrokes |
| **Flag** | `BVAULT{usb_k3ystr0k3s_r3c0v3r3d}` |
| **⚠️ Warning** | Contains jump-scare audio/visual element in artifact |

**Solve summary:**
1. Filter in Wireshark: `usb.transfer_type == 0x01` (Interrupt — HID)
2. Extract `HID Data` field bytes
3. Map USB HID keycodes → ASCII characters
4. Reconstruct typed text → flag

**Extract HID data:**
```bash
tshark -r usb_capture.pcap -T fields -e usb.capdata 2>/dev/null \
  | sed '/^\s*$/d' | python3 usb_hid_decode.py
```

---

### Challenge 06 — Schizophrenic Malware 🔴 Hard

| Field | Value |
|-------|-------|
| **Files** | `malware.pcap` + `memory.dmp` |
| **Concept** | DNS exfiltration malware — network + memory forensics combo |
| **Flag** | `BVAULT{sch1z0phr3n1c_m4lw4r3_4n4lyz3d}` |
| **⚠️ Warning** | Memory dump contains simulated horror-themed strings |

**Solve summary (two-part):**

*Part 1 — Network (PCAP):*
```bash
# Extract DNS query subdomains (exfiltrated data)
tshark -r malware.pcap -T fields -e dns.qry.name \
  | grep -v '#' | sort -u | python3 dns_decode.py
```

*Part 2 — Memory (Volatility3):*
```bash
vol -f memory.dmp windows.pslist  # or linux.pslist
vol -f memory.dmp windows.cmdline
vol -f memory.dmp windows.filescan | grep flag
vol -f memory.dmp windows.dumpfiles --physaddr <addr>
```

---

## Psychological Horror Elements

> The following challenges contain intentional horror theming:

| Challenge | Element |
|-----------|---------|
| 05 — Polymorphic Nightmare | Audio jump-scare embedded in USB keystrokes |
| 06 — Schizophrenic Malware | Horror-themed strings in memory dump |

**Organizer action:** Add a content warning in the CTFd challenge description before the event starts.

---

## Common Participant Issues

| Issue | Solution |
|-------|---------|
| Can't open `.img` file | Check file size — may need `sudo mount` or `testdisk` |
| PCAP shows no HTTP traffic | Check for HTTPS — decrypt with provided key if applicable |
| Volatility plugin errors | Ensure correct profile: `vol -f mem.dmp banners.Banners` |
| USB HID decode wrong | Verify modifier bytes are handled (Shift key for capitals) |
