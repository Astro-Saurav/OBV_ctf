# Challenge 05: The Ghost VM

**Concept:** Custom Virtual Machine (VM) Obfuscation
**Difficulty:** 🔴 Hard

## Objective
The player is given a C binary (`ghost_vm.elf`) and a bytecode file (`vault_logic.bin`). The goal is to reverse engineer the C binary to map out the VM's custom opcodes, then write a disassembler for the bytecode to recover the password.

## Solution

### 1. Reversing the VM Engine
Opening `ghost_vm.elf` in Ghidra/IDA, we see a massive `switch(opcode)` statement inside an execution loop.
By analyzing the stack operations (`stack[++sp]`, `stack[sp--]`), we can map the Instruction Set Architecture (ISA):

- `0x01`: PUSH (takes 1 byte argument)
- `0x02`: POP to Register A
- `0x03`: POP to Register B
- `0x04`: ADD (A + B, pushes to stack)
- `0x05`: SUB (A - B, pushes to stack)
- `0x06`: XOR (A ^ B, pushes to stack)
- `0x07`: CMP (sets internal flag if A == B)
- `0x08`: JZ (Jump to argument address if CMP flag is 1)
- `0x09`: JMP (Unconditional jump)
- `0x0A`: READ (Reads 1 char from user input into stack)
- `0x0B`: SUCC (Prints Flag and exits)
- `0x0C`: FAIL (Prints Denied and exits)
- `0x0D`: HALT

### 2. Disassembling the Bytecode
We can write a quick Python script to read `vault_logic.bin` and print the assembly based on our mapped ISA.

```python
with open("vault_logic.bin", "rb") as f:
    code = f.read()

opcodes = {1:"PUSH", 2:"POP_A", 3:"POP_B", 4:"ADD", 5:"SUB", 
           6:"XOR", 7:"CMP", 8:"JZ", 9:"JMP", 10:"READ", 
           11:"SUCC", 12:"FAIL", 13:"HALT"}

i = 0
while i < len(code):
    op = code[i]
    if op in [1, 8, 9]: # Takes an argument
        print(f"{i:02x}: {opcodes[op]} 0x{code[i+1]:02x}")
        i += 2
    else:
        print(f"{i:02x}: {opcodes[op]}")
        i += 1
```

### 3. Reversing the Bytecode Logic
Running our disassembler yields a repeating pattern for 7 characters. For example, the first block is:
```
00: READ
01: PUSH 0x42
03: POP_B
04: POP_A
05: XOR
06: POP_A
07: PUSH 0x11
09: POP_B
0a: CMP
0b: JZ 0x0e
0d: FAIL
```
It reads a char, pushes `0x42` (66) to the stack. Pops them into A and B, XORs them, and compares the result to `0x11` (17). 
So: `input[0] ^ 66 = 17` $\rightarrow$ `input[0] = 17 ^ 66 = 83 ('S')`.

Following this logic for the remaining blocks:
- `0x11 ^ 0x42 = 83` (S)
- `0x0E ^ 0x42 = 80` (P)
- `0x03 ^ 0x42 = 69` (E)
- `0x01 ^ 0x42 = 67` (C)
- `0x12 ^ 0x42 = 84` (T)
- `0x10 ^ 0x42 = 82` (R)
- `0x03 ^ 0x42 = 69` (E)

The access code is `SPECTRE`.

### Execution
```bash
$ ./ghost_vm.elf SPECTRE
Operation Black Vault - Ghost VM CPU v1.0
Access Granted. Flag: BVAULT{gh057_vm_r3v3r53d_5ucc355fully}
```

## Flag
`BVAULT{gh057_vm_r3v3r53d_5ucc355fully}`
