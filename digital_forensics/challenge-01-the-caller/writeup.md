# challenge-01-the-caller

**Concept:** Audio Steganography (DTMF Tones)
**Difficulty:** 🟢 Easy

## Solution

The file `voicemail.wav` contains a jump scare at 3 seconds, followed by faint robotic dial tones (DTMF tones). 
If you analyze the audio (e.g., using a DTMF decoder tool or spectral analysis), you can extract the sequence of button presses.
The DTMF tones represent the ASCII decimal values of the flag characters, separated by the `*` key.

Example Python decoder using `dtmf-decoder` or simple mapping:
```python
# The sequence is: 66*86*65*85*76*84*123*100*55*109*102*95*55*48*110*51*53*95*52*114*51*95*99*114*51*51*112*121*125
tones = "66*86*65*85*76*84*123*100*55*109*102*95*55*48*110*51*53*95*52*114*51*95*99*114*51*51*112*121*125"
flag = "".join([chr(int(x)) for x in tones.split('*')])
print(flag)
```
## Flag
`BVAULT{d7mf_70n35_4r3_cr33py}`
