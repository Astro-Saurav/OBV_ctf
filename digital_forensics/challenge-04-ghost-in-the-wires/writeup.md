# challenge-04-ghost-in-the-wires

**Concept:** PCAP Analysis & HTTP Extraction
**Difficulty:** 🟡 Medium

## Solution

The PCAP contains hundreds of junk UDP packets. 
Filter by `http` in Wireshark. You will see a GET request for `/ghost.gif`.
1. Go to **File -> Export Objects -> HTTP**.
2. Save the `ghost.gif` file.
3. The image is a creepy jump-scare GIF. However, if you inspect the raw bytes of the GIF (using a Hex Editor or the `strings` command), the flag is appended immediately after the GIF EOF trailer (`3B`).

```bash
strings ghost.gif | grep BVAULT
```

## Flag
`BVAULT{gh057_1n_7h3_pc4p_n37w0rk}`
