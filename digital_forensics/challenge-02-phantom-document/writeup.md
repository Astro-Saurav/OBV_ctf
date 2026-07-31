# challenge-02-phantom-document

**Concept:** Invisible Ink & Metadata
**Difficulty:** 🟢 Easy

## Solution

If you open `briefing.pdf` and select all text (`Ctrl+A`), you'll discover thousands of hidden lines that read "I AM BEHIND YOU" written in white ink on a white background.
However, the flag isn't in the text. 
To find the actual flag, you must use a tool like `exiftool` to inspect the document's metadata (specifically the embedded XMP CreatorTool/Author fields).

```bash
exiftool briefing.pdf | grep BVAULT
# Creator Tool : BVAULT{ph4n70m_m374d474_r3v34l3d}
```
## Flag
`BVAULT{ph4n70m_m374d474_r3v34l3d}`
