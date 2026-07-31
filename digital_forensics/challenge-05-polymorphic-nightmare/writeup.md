# challenge-05-polymorphic-nightmare

**Concept:** Polyglot Files & Hex Editing
**Difficulty:** 🔴 Hard

## Solution

The file `nightmare` is a Polyglot: it is both a valid PNG image and a valid ZIP archive.
1. Rename it to `nightmare.zip` and attempt to unzip it. You will see it contains a file, but it asks for a password.
2. The password is hidden inside the PNG structure. 
3. Open `nightmare` in a Hex Editor. Inspect the PNG chunks immediately following the IHDR chunk. You will find a custom chunk named `scAr` containing the string `P4ssw0rd_Fr0m_H3ll!`.
4. Use this password to unzip the archive and retrieve the flag.

## Flag
`BVAULT{p0lygl07_f1l35_4r3_n1gh7m4r35}`
