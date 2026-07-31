# Challenge 03: The Chronos Anomaly

**Concept:** Time-Delta Network Covert Channels
**Difficulty:** 🟠 Medium/Hard

## Objective
Players receive a tiny `capture.pcap` file containing a few dozen standard ICMP Ping requests. The payloads are empty and the source/destination IPs are normal. The data is hidden in a network covert channel: the **inter-packet timing**.

## Solution
If a player observes the packet timestamps very closely in Wireshark (by changing the time display format to "Seconds Since Previous Captured Packet"), they will notice a pattern.

The delay between packet 1 and packet 2 is `0.066` seconds.
The delay between packet 2 and packet 3 is `0.086` seconds.
The delay between packet 3 and packet 4 is `0.065` seconds.

These time delays correspond exactly to the ASCII decimal values of the hidden message!
`0.066` seconds * 1000 = `66` = `B`
`0.086` seconds * 1000 = `86` = `V`
`0.065` seconds * 1000 = `65` = `A`

To solve this efficiently, players must write a parser using `scapy` or `pyshark` to extract the timestamps, calculate the deltas, multiply by 1000, and convert them to ASCII.

### Exploit Script (test_exploit.py)
```python
from scapy.all import rdpcap, ICMP

packets = rdpcap('capture.pcap')
flag = ""

# Start from index 1 to compare with the previous packet
for i in range(1, len(packets)):
    if packets[i].haslayer(ICMP):
        delta = float(packets[i].time - packets[i-1].time)
        ascii_val = int(round(delta * 1000))
        
        # Ignore randomized large deltas at the end of the capture
        if ascii_val < 127:
            flag += chr(ascii_val)

print(flag)
```

## Flag
`BVAULT{t1m3_15_4n_1llu510n}`
