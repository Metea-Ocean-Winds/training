# Bash Scripting Guide

---

# Script Skeleton

```bash
#!/bin/bash
set -euo pipefail

usage() {
    echo "Usage: $0 <file>" >&2
    exit 1
}

[[ $# -lt 1 ]] && usage
file="$1"

echo "Processing $file"
```

```bash
chmod +x script.sh     # make executable
./script.sh            # run
bash -x script.sh      # run with debug trace
shellcheck script.sh   # lint
```

---

# Variables

```bash
name="value"           # no spaces around =
echo "$name"           # always quote
echo "${name}_suffix"  # braces when followed by text
today=$(date +%F)      # command substitution
total=$((a + b))       # arithmetic
top="${2:-5}"          # default value if $2 is empty
```

---

# Special Variables

| Variable | Meaning                         |
| -------- | ------------------------------- |
| `$0`     | Script name                     |
| `$1..$9` | Positional arguments            |
| `$#`     | Number of arguments             |
| `$@`     | All arguments (use `"$@"`)      |
| `$?`     | Exit code of last command       |
| `$$`     | PID of the script               |
| `$EUID`  | Effective user ID (0 = root)    |

---

# Input

```bash
read -p "Name: " name          # prompt
read -s -p "Password: " pass   # hidden input
```

---

# Conditions

```bash
if [[ -f "$file" ]]; then
    echo "file"
elif [[ -d "$file" ]]; then
    echo "directory"
else
    echo "missing"
fi
```

| File          | String           | Number          |
| ------------- | ---------------- | --------------- |
| `-e` exists   | `==` equal       | `-eq` equal     |
| `-f` file     | `!=` different   | `-ne` not equal |
| `-d` dir      | `-z` empty       | `-gt` greater   |
| `-r` readable | `-n` not empty   | `-lt` less      |
| `-x` executable |                | `-ge` / `-le`   |
| `-s` not empty |                 |                 |

```bash
[[ cond1 && cond2 ]]           # AND
[[ cond1 || cond2 ]]           # OR
[[ ! cond ]]                   # NOT
(( count > 10 ))               # numeric comparison
if grep -q ERROR "$file"; then # any command's exit code
```

---

# Loops

```bash
for x in a b c; do echo "$x"; done
for f in *.log; do echo "$f"; done
for i in {1..10}; do echo "$i"; done
for ((i=0; i<5; i++)); do echo "$i"; done

while read -r line; do
    echo "$line"
done < file.txt

while [[ $n -gt 0 ]]; do
    n=$((n - 1))
done
```

`break` exits the loop · `continue` skips to the next iteration

---

# Functions

```bash
greet() {
    local who="$1"
    echo "Hello $who"
    return 0
}

greet "Ana"
result=$(greet "Ben")
```

---

# Exit Codes & Errors

```bash
exit 0                          # success
exit 1                          # failure
echo "Error!" >&2               # print to stderr
cmd && echo ok || echo failed
grep -c X file || true          # tolerate "no match" with set -e
```

---

# Useful Snippets

```bash
timestamp=$(date +%F_%H%M)                 # 2026-10-15_1030
mkdir -p "$dir"                            # create if missing
[[ $EUID -ne 0 ]] && { echo "Run as root" >&2; exit 1; }
ln -sfn "$new_file" latest                 # update a symlink
ls -1t backup_*.tar.gz | tail -n +6        # all but newest 5
```

---

# Cron

See [crontab_guide.md](crontab_guide.md). Remember: absolute paths and `>> log 2>&1`.
