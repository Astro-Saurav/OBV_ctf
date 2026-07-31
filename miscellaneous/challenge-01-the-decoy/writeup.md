# Challenge 01: The Decoy

**Concept:** Anti-AI Traps & Basic Version Control
**Difficulty:** 🟢 Easy

## Objective
The player is given a `repo.zip` archive containing a file named `flag.txt`. 

When the player opens `flag.txt`, they find a massive block of text explicitly designed to manipulate AI assistants and Large Language Models into outputting a fake flag (`BVAULT{th1s_1s_4_f4k3_fl4g}`). If a player blindly feeds the file into an LLM to solve the challenge for them, they will be given the wrong answer.

However, the ZIP file also contains a hidden `.git` directory. The real flag was stored in the initial commit, and then overwritten with the fake AI prompt in a subsequent commit.

## Solution

1. Extract the `repo.zip` file.
2. Notice the presence of a hidden `.git` folder indicating this is a Git repository.
3. Run `git log -p` or use a tool like `gitk` / `git log --stat` to view the commit history.
4. The initial commit (`Initialize project and store secure flag`) shows the addition of the real flag.

```bash
$ git log -p
...
commit f6a9a500c4ee4f1e279a3845b57b33ff47912aff
Author: root <root@blackvault>
Date:   ...

    Initialize project and store secure flag

diff --git a/flag.txt b/flag.txt
new file mode 100644
index 0000000..069fa42
--- /dev/null
+++ b/flag.txt
@@ -0,0 +1 @@
+BVAULT{m4573r_0f_v3r510n_c0n7r0l}
```

### Exploit Script (test_exploit.sh)
```bash
#!/bin/bash
unzip -q repo.zip -d extracted_repo
cd extracted_repo
git log -p | grep "BVAULT{" | tail -n 1 | awk '{print $1}' | tr -d '+'
cd ..
rm -rf extracted_repo
```

## Flag
`BVAULT{m4573r_0f_v3r510n_c0n7r0l}`
