# challenge-03-cursed-disk

**Concept:** File Carving & Deleted Data
**Difficulty:** 🟡 Medium

## Solution

If you mount `cursed.img` normally, you won't see the deleted file.
You must use a forensic carving tool like `binwalk` or `photorec` to extract the deleted zip file from the unallocated space.

Using `binwalk`:
```bash
binwalk -e cursed.img
```
Inside the extracted directory, you will find a valid ZIP file that contains `flag.txt`.
Alternatively, you can use the Sleuthkit (`fls` and `icat`) to recover the file.

## Flag
`BVAULT{d3l373d_f1l35_n3v3r_d13}`
