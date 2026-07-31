# Challenge 06: Deep Root

**Concept:** Real-world Malware Behavior / Log Parsing / Environmental Keys
**Difficulty:** 🔴 Very Hard

## Objective
The player is given a compiled Linux binary (`backdoor_daemon.elf`) and a log file (`recovered_sys.log`). The binary expects a specific file in its directory to execute correctly. It parses this file for specific environmental indicators (an IP address) to use as an encryption key. The player must reverse the binary, understand its environmental expectations, and recover the flag.

## Solution

### 1. Reversing the Backdoor
When you run `backdoor_daemon.elf`, nothing happens. It immediately exits silently.

If you open the binary in Ghidra/IDA or use `strace ./backdoor_daemon.elf`, you will notice it attempts to open a file:
```bash
$ strace ./backdoor_daemon.elf
...
openat(AT_FDCWD, "system_auth.log", O_RDONLY) = -1 ENOENT (No such file or directory)
exit_group(0)                           = ?
+++ exited with 0 +++
```
The binary expects a file named `system_auth.log`. We were given `recovered_sys.log`. So the first step is to rename or symlink the file.
```bash
$ cp recovered_sys.log system_auth.log
```
Running it again still produces no output.

### 2. Static Analysis of the Parser
Looking at the decompiled code in Ghidra, we see:
```c
  f = fopen("system_auth.log","r");
  if (f == (FILE *)0x0) {
    return 0;
  }
  // ...
  while (fgets(line, 512, f) != (char *)0x0) {
    if (strstr(line, "Accepted password for root from") != (char *)0x0) {
        // ... extracts the string after "from " until the next space
    }
  }
```
The binary is searching for a successful root login via password. 
Looking at our log file:
```
Jul 31 16:12:00 vault-srv sshd[901]: Accepted password for root from 10.99.0.222 port 50123 ssh2
```
The extracted string will be the IP address: `10.99.0.222`.

### 3. Decrypting the Flag
The binary uses this IP string as a cyclic XOR key against a hardcoded byte array in memory:
`{0x73, 0x66, 0x6f, 0x6c, 0x75, 0x7a, ...}`

You can write a Python script to do this offline:
```python
key = b"10.99.0.222"
enc = bytes([0x73, 0x66, 0x6f, 0x6c, 0x75, 0x7a, 0x4b, 0x1d, 0x5c, 0x44, 0x03, 0x43, 0x00, 0x40, 0x54, 0x0a, 0x40, 0x07, 0x1a, 0x5e, 0x6d, 0x59, 0x02, 0x49, 0x1f, 0x57, 0x5e, 0x71, 0x01, 0x1b, 0x6d, 0x07, 0x05, 0x02, 0x04, 0x42, 0x0e, 0x51, 0x57, 0x4d])

flag = bytes([enc[i] ^ key[i % len(key)] for i in range(len(enc))])
print(flag.decode())
```

### Alternative: Dynamic Execution
If you look further down the decompiled C code, the binary will actually print the decrypted flag if you pass the `--debug` argument!

```bash
$ ./backdoor_daemon.elf --debug
Vault connection established: BVAULT{3nv1r0nm3n74l_k3y1ng_15_5734l7hy}
```

## Flag
`BVAULT{3nv1r0nm3n74l_k3y1ng_15_5734l7hy}`
