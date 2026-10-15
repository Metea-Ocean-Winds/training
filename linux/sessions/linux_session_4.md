# 📜 Session 4 – Bash Scripting

**Duration:** 90 minutes

**Theme:** Stop typing the same commands. Write them once, run them forever.

---

# 🎯 Objectives

By the end of this session you should be able to:

- Write, make executable and run a bash script
- Use variables, arguments and user input
- Make decisions with `if` and tests
- Repeat work with `for` and `while` loops
- Organise code into simple functions
- Return meaningful exit codes
- Schedule a script with `crontab`

---

# 🧾 1. What Is a Script?

A script is just a text file with commands, executed from top to bottom.

Everything you type in the terminal can go into a script.

***Your first script***

```bash
nano hello.sh
```

```bash
#!/bin/bash
# Prints a greeting
echo "Hello, $USER"
echo "Today is $(date +%A)"
```

***The shebang***

The first line `#!/bin/bash` tells Linux **which program** must run the file.

***Run it***

```bash
bash hello.sh        # option 1: ask bash to run it

chmod +x hello.sh    # option 2: make it executable...
./hello.sh           # ...and run it
```

> *Why `./`?*
> 
> The current folder is not in your `PATH`. `./` means "the file in this folder".

***Run it from anywhere***

```bash
mkdir -p ~/bin
mv hello.sh ~/bin/hello
hello                # works if ~/bin is in your PATH (default on Ubuntu after re-login)
```

---

# 💲 2. Variables

```bash
#!/bin/bash
name="Wizard"
log_file="/var/log/syslog"
count=$(wc -l < "$log_file")

echo "Hello $name"
echo "$log_file has $count lines"
```

Rules:

- No spaces around `=`
- Read with `$name` or `${name}`
- Always quote: `"$name"`

***Arithmetic***

```bash
a=7
b=3
echo $((a + b))      # 10
echo $((a * b))      # 21
echo $((a / b))      # 2   (integers only)
echo $((a % b))      # 1   (remainder)
```

---

# 📥 3. Input: Arguments & read

## Arguments

```bash
./report.sh app.log 10
```

| Variable | Value                          |
| -------- | ------------------------------ |
| `$0`     | Script name (`./report.sh`)    |
| `$1`     | First argument (`app.log`)     |
| `$2`     | Second argument (`10`)         |
| `$#`     | Number of arguments (`2`)      |
| `$@`     | All arguments                  |

```bash
#!/bin/bash
echo "Script: $0"
echo "File:   $1"
echo "Top:    $2"
echo "Total arguments: $#"
```

***Default values***

```bash
top="${2:-5}"        # use $2, or 5 if it was not given
```

## read

```bash
#!/bin/bash
read -p "What is your name? " name
echo "Welcome, $name"
```

---

# 🔀 4. Conditions

```bash
if [[ condition ]]; then
    ...
elif [[ other_condition ]]; then
    ...
else
    ...
fi
```

> Spaces inside `[[ ` and ` ]]` are **mandatory**.

## Tests

| File tests    | True if…                 |
| ------------- | ------------------------ |
| `-e file`     | exists                   |
| `-f file`     | is a regular file        |
| `-d dir`      | is a directory           |
| `-r file`     | is readable              |
| `-x file`     | is executable            |
| `-s file`     | is not empty             |

| String tests  | True if…                 |
| ------------- | ------------------------ |
| `"$a" == "$b"`| equal                    |
| `"$a" != "$b"`| different                |
| `-z "$a"`     | empty                    |
| `-n "$a"`     | not empty                |

| Number tests  | Meaning                  |
| ------------- | ------------------------ |
| `-eq` `-ne`   | equal / not equal        |
| `-gt` `-ge`   | greater / greater-equal  |
| `-lt` `-le`   | less / less-equal        |

> *Why not `>` for numbers?* Inside `[[ ]]`, `>` compares **text** alphabetically. Use `-gt`, or `(( a > b ))`.

***Example***

```bash
#!/bin/bash
file="$1"

if [[ -z "$file" ]]; then
    echo "Usage: $0 <logfile>"
    exit 1
elif [[ ! -f "$file" ]]; then
    echo "Error: $file does not exist"
    exit 2
fi

errors=$(grep -c ERROR "$file")

if [[ $errors -gt 100 ]]; then
    echo "🔥 $errors errors – investigate!"
else
    echo "✅ $errors errors – acceptable"
fi
```

***Conditions with commands***

`if` actually checks an **exit code**. Any command works:

```bash
if grep -q CRITICAL "$file"; then
    echo "Critical entries found"
fi
```

---

# 🔁 5. Loops

## for – over a list

```bash
for level in ERROR WARNING INFO DEBUG; do
    echo "$level: $(grep -c "$level" app.log)"
done
```

## for – over files

```bash
for f in *.log; do
    echo "$f has $(wc -l < "$f") lines"
done
```

## for – over a range

```bash
for i in {1..5}; do
    echo "Attempt $i"
done
```

## while read – line by line

```bash
while read -r ip; do
    echo "Checking $ip"
done < ip_list.txt
```

```bash
grep ERROR app.log | awk '{print $4}' | sort -u | while read -r ip; do
    echo "Blocking $ip (not really)"
done
```

---

# 🧩 6. Functions

Group commands under a name. Call them like any other command.

```bash
#!/bin/bash

count_level() {
    local level="$1"
    local file="$2"
    grep -c "$level" "$file"
}

log() {
    echo "[$(date +%T)] $*"
}

log "Starting analysis"
log "Errors: $(count_level ERROR app.log)"
log "Warnings: $(count_level WARNING app.log)"
```

- Arguments inside a function are `$1`, `$2`… (the function's own)
- `local` keeps variables inside the function

---

# 🚪 7. Exit Codes

Your script should tell the world whether it worked.

```bash
exit 0     # success
exit 1     # generic failure
```

```bash
./report.sh app.log && echo "Report OK" || echo "Report FAILED"
```

---

# ✅ 8. Good Habits

```bash
#!/bin/bash
set -euo pipefail
```

| Option        | Effect                                              |
| ------------- | --------------------------------------------------- |
| `-e`          | Stop at the first failing command                   |
| `-u`          | Using an undefined variable is an error             |
| `-o pipefail` | A pipeline fails if **any** command in it fails     |

> *Careful*: with `-e`, `grep` returning "no match" (exit code 1) stops the script. Use `grep ... || true` when "no match" is acceptable.

Checklist:

- Quote your variables: `"$file"`
- Validate arguments at the start
- Use comments for the *why*, not the *what*
- Use absolute paths in scripts that run automatically
- Check your script with `shellcheck`:

```bash
sudo apt install shellcheck
shellcheck report.sh
```

***Debugging***

```bash
bash -x report.sh app.log    # prints every command before running it
```

---

# ⏰ 9. Scheduling with crontab

Scripts become powerful when they run on their own.

```bash
crontab -e
```

```
# ┌ minute ┌ hour ┌ day ┌ month ┌ weekday
  */5      *      *     *       *        /home/alice/bin/report.sh /home/alice/logs/app.log >> /home/alice/logs/report.log 2>&1
  0        2      *     *       *        /home/alice/bin/backup.sh >> /home/alice/logs/backup.log 2>&1
```

***Cron is not your terminal***

| In your terminal            | In cron                                 |
| --------------------------- | --------------------------------------- |
| You are in some folder      | Working directory is your home          |
| Full `PATH`                 | Minimal `PATH` (`/usr/bin:/bin`)        |
| Output on screen            | Output is lost unless you redirect it   |
| Your aliases exist          | No aliases, no `.bashrc`                |

So:

- Use **absolute paths** everywhere
- Always redirect output: `>> file.log 2>&1`
- Test the exact cron line in the terminal first

```bash
crontab -l     # list your jobs
crontab -r     # remove ALL your jobs (careful!)
```

See also: [crontab guide](../cheat-sheet/crontab_guide.md)

---

# In the next session ...

Time to put on the administrator hat:

- Users, groups and `sudo`
- The sudoers file
- Disks, partitions and mounting
