# Challenge 02: Polyglot Paradox

**Concept:** Polyglot Files & Steganography
**Difficulty:** 🟡 Medium

## Objective
The player is given a file named `classified_document.pdf`. This file is a polyglot: it is simultaneously a valid PDF document, a valid ZIP archive, and a valid Python script (specifically a Python zipapp).

If the player opens the file in a PDF viewer, they see a fake flag: `BVAULT{f4k3_pdf_fl4g}`.
If the player runs the file as a Python script (`python3 classified_document.pdf`), they get an anti-AI prompt with another fake flag: `BVAULT{th1s_1s_4_f4k3_fl4g_p0lygl07}`.

To find the real flag, players must realize the file is also a ZIP archive.

## Solution

1. Run `file classified_document.pdf` or use `binwalk` to discover the hidden ZIP structure at the end of the file.
2. Extract the ZIP archive:
   ```bash
   unzip classified_document.pdf
   ```
   *Note: This will extract two files: `secret.jpg` and `__main__.py`.*
3. Analyze `secret.jpg`. Running `strings secret.jpg` or `exiftool secret.jpg` reveals a strange string in the ImageDescription / Comment EXIF tag:
   ```
   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++.--------------------------------------------------.+++++++++++++++.+++++++++++++++++++++++++++++++.----------------------------------------------------.+++++++++++++++++++++++++++++++++++++++++++++++++++.---.+++++++++++++++++++++++++++++.---------------------------------------------------.++++++++++++++++++++++++++++++++++++++++++++++++++.----------------.++++++++++++++++++++++++.---------------------------------------.++++++++++++++++++++++++++++++++++++++.++++.-----------------------------------------.+++++++++++++++++++++++++++++++++++++++.---------------------------------------.++++++++++++++++++++++++++++++++++++++.++++++++++++.--------------------------------------------------.+++++++++++++++++++++++++++++++++++++++++++++++++.--------------------------------------------------.+++++++++++++++++++++++++++++++++++++++++++++++++.
   ```
4. Recognize the string as **Brainfuck** esoteric programming language code.
5. Decode the Brainfuck code using an online interpreter or local script to reveal the true flag.

### Exploit Script (test_exploit.py)
```python
import zipfile
import subprocess
import piexif

def brainfuck_to_text(bf_code):
    text = ""
    curr = 0
    for char in bf_code:
        if char == '+':
            curr += 1
        elif char == '-':
            curr -= 1
        elif char == '.':
            text += chr(curr)
    return text

with zipfile.ZipFile('classified_document.pdf', 'r') as z:
    z.extract('secret.jpg', '/tmp/')

exif_dict = piexif.load('/tmp/secret.jpg')
bf_code = exif_dict["0th"][piexif.ImageIFD.ImageDescription].decode('utf-8')
print(brainfuck_to_text(bf_code))
```

## Flag
`BVAULT{m4573r_0f_m4ny_l4ngu4g35}`
