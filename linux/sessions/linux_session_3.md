# 🔁 Session 3 – Flashback & Shell Power-Ups

**Duration:** 90 minutes

**Theme:** Remember what you know, then make the shell work for you

---

# 🎯 Objectives

By the end of this session you should be able to:

- Recall the key ideas and commands from Sessions 1 and 2
- Find help on any command without leaving the terminal
- Use variables, quoting, wildcards and command substitution
- Chain commands using exit codes (`&&`, `||`)
- Use `tr`, `tee`, `diff` and `less`
- Create and extract archives with `tar` and `gzip`
- Control jobs and reuse your command history

---

# 🧠 1. Flashback – Session 1

| Concept          | Remember                                                    |
| ---------------- | ----------------------------------------------------------- |
| **Kernel**       | The core. Talks to the hardware (CPU, memory, disks)        |
| **Distribution** | Kernel + tools + package manager (Ubuntu, Debian, Fedora…)  |
| **Terminal**     | The text window you type into                               |
| **Shell**        | The program that interprets your commands (`bash`)          |
| **Philosophy**   | Everything is a file · small tools · combine them · text    |

***Permissions***

```
-rwxr-xr-- 1 alice dev 4096 Jan 10 12:00 script.sh
 │  │  │
 │  │  └── others : r--  = 4
 │  └───── group  : r-x  = 5
 └──────── user   : rwx  = 7     → chmod 754 script.sh
```

```bash
chmod u+x file          # symbolic mode
chmod 640 file          # octal mode
sudo chown user:group file
```

***Shortcuts you should already be using***

| Shortcut   | Action                         |
| ---------- | ------------------------------ |
| `Tab`      | Autocomplete                   |
| `Ctrl + R` | Search history                 |
| `Ctrl + A` | Beginning of line              |
| `Ctrl + E` | End of line                    |
| `Ctrl + U` | Cut to beginning of line       |
| `!!`       | Repeat last command            |
| `!$`       | Last argument of last command  |

---

# 🧙 2. Flashback – Session 2

| Tool                  | One-line reminder                                        |
| --------------------- | -------------------------------------------------------- |
| `find`                | Search files by name, type, size, time                   |
| `grep`                | Search text inside files (`-i -n -v -c -r -E`)           |
| `sed`                 | Stream editor: replace (`s///g`), delete (`/x/d`)        |
| `cut`                 | Simple columns with a single separator (`-d -f`)         |
| `awk`                 | Fields, conditions, irregular spacing (`$1`, `$NF`)      |
| `sort / uniq / wc`    | Rank and count (`sort \| uniq -c \| sort -nr`)           |
| `xargs`               | Turn text from a pipe into arguments                     |
| `ps / kill / nohup &` | Inspect, stop and detach processes                       |
| `> >> 2>&1`           | Overwrite, append, merge errors                          |
| `ln -s`               | Symbolic link                                            |

The mental model is still the same:

```
file → command → command → command → result
```

---

# ✍ 3. Warm-up Quiz

Answer without running anything. Then check.

1. What octal value gives `rw-r-----`?
2. Which `grep` flag counts matches instead of printing them?
3. What is the difference between `>` and `>>`?
4. What is wrong with `awk '$7 = 500 {print $0}' app.log`?
5. Why does `find . -name "*.log" | grep ERROR` not search inside the logs?
6. Which command shows processes in real time?
7. What does `2>/dev/null` do?
8. Which `sed` command prints only line 5?
9. What does `uniq` need before it to work correctly?
10. You ran `mkdir /very/long/path`. How do you `cd` into it without retyping?

<details>
<summary>Answers</summary>

1. `640`
2. `grep -c`
3. `>` overwrites the file, `>>` appends to it
4. `=` assigns instead of compares. Use `==`
5. `grep` searches the file *names*, not their content. Use `xargs grep ERROR`
6. `top` (or `htop`)
7. Throws away error messages (stderr)
8. `sed -n '5p' file`
9. `sort` – `uniq` only removes *adjacent* duplicates
10. `cd !$`

</details>

---

# 🧩 4. Pipeline Puzzles

Use `app.log` and `process.log` from the `images/` folder.

Reminder of the format:

```
2025-02-14 08:00:35 ERROR 161.29.39.109 "GET /dashboard" 500 - Unhandled exception
   $1        $2      $3       $4          $5      $6      $7  $8  ...

2025-02-14 08:00:00 PROCESS payment-service CPU=31% MEM=239MB STATUS=RESTARTING
   $1        $2       $3          $4           $5      $6          $7
```

1. Which endpoint (`/login`, `/dashboard`, …) appears most often?
2. How many **different** IPs produced an `ERROR`?
3. Which process name has the most `STATUS=RESTARTING` entries?
4. List the 3 most frequent error messages.
5. How many lines contain a `404` on `/api/data`?

<details>
<summary>Possible solutions</summary>

```bash
awk '{print $6}' app.log | tr -d '"' | sort | uniq -c | sort -nr | head -1
grep ERROR app.log | awk '{print $4}' | sort -u | wc -l
grep RESTARTING process.log | awk '{print $4}' | sort | uniq -c | sort -nr | head -1
grep ERROR app.log | sed 's/.* - //' | sort | uniq -c | sort -nr | head -3
grep '/api/data' app.log | grep -c ' 404 '
```

There is always more than one valid pipeline.

</details>

---

# 🆘 5. Getting Help

You don't need to memorise every flag. You need to know where to look.

```bash
man grep            # full manual (q to quit, / to search inside)
grep --help         # short summary
apropos partition   # search manuals by keyword
type ls             # is it a builtin, an alias or a program?
which python3       # where is the program on disk?
```

> *Trick*
> 
> Inside `man`, type `/-v` and press `Enter` to jump to the `-v` flag. Press `n` for the next match.

---

# 💲 6. Shell Essentials

## Variables

```bash
name="wizard"        # no spaces around =
echo $name
echo "Hello $name"
```

## Environment variables

Environment variables are visible to every program you start.

```bash
echo $HOME
echo $USER
echo $PATH           # where the shell looks for programs
env                  # list all of them
export EDITOR=nano   # make a variable visible to child programs
```

`PATH` is a list of folders separated by `:`. When you type `ls`, the shell searches those folders in order.

```bash
echo $PATH | tr ':' '\n'
```

## Quoting

| Syntax     | Behaviour                                           |
| ---------- | --------------------------------------------------- |
| `'text'`   | Literal. Nothing is expanded                        |
| `"text"`   | Variables and `$(...)` are expanded                 |
| `\`        | Escapes the next character                          |

```bash
echo '$HOME'         # $HOME
echo "$HOME"         # /home/alice
echo "Price: \$5"    # Price: $5
```

> *Rule of thumb*
> 
> Always wrap variables in double quotes: `"$file"`. File names with spaces will thank you.

## Wildcards (globbing)

```bash
ls *.log             # any number of characters
ls file?.txt         # exactly one character
ls report[1-3].txt   # one character from a range
```

## Brace expansion

```bash
mkdir -p project/{src,docs,tests}
touch day{1..5}.txt
cp config.yml{,.bak}   # same as: cp config.yml config.yml.bak
```

## Command substitution

Run a command and use its output as text.

```bash
echo "Today is $(date +%F)"
errors=$(grep -c ERROR app.log)
echo "There are $errors errors"
```

---

# 🚦 7. Exit Codes & Chaining

Every command returns an **exit code**:

- `0` → success
- anything else → failure

```bash
ls /etc
echo $?        # 0

ls /nope
echo $?        # 2
```

Use exit codes to chain commands:

| Operator | Runs the next command…            |
| -------- | --------------------------------- |
| `;`      | always                            |
| `&&`     | only if the previous **succeeded**|
| `\|\|`   | only if the previous **failed**   |

```bash
mkdir backup && cp app.log backup/
grep -q CRITICAL app.log || echo "No critical errors"
cd /tmp; ls
```

> `grep -q` prints nothing. It only sets the exit code. Perfect for conditions.

This is the foundation of scripting (Session 4).

---

# 🛠 8. More Text Tools

## tr – translate characters

```bash
echo "hello" | tr 'a-z' 'A-Z'      # HELLO
echo "a,b,c" | tr ',' '\n'         # one per line
tr -d '"' < app.log                # delete quotes
tr -s ' ' < file.txt               # squeeze repeated spaces
```

## tee – see it AND save it

```bash
grep ERROR app.log | tee errors.txt | wc -l
```

The output goes to the screen (or next command) and to `errors.txt` at the same time.

```bash
command | tee -a run.log           # append instead of overwrite
```

## diff – compare files

```bash
diff old.txt new.txt
diff -u old.txt new.txt            # unified format (like git)
```

## less – a better `more`

```bash
less app.log
```

| Key         | Action           |
| ----------- | ---------------- |
| `Space`/`b` | Page down / up   |
| `/word`     | Search forward   |
| `n` / `N`   | Next / previous  |
| `G` / `g`   | End / start      |
| `q`         | Quit             |

---

# 📦 9. Archives & Compression

`tar` bundles many files into one. `gzip` compresses.

```bash
tar -czf logs.tar.gz *.log     # create (c) + gzip (z) + file (f)
tar -tzf logs.tar.gz           # list contents (t)
tar -xzf logs.tar.gz           # extract (x)
tar -xzf logs.tar.gz -C /tmp   # extract into another folder
```

> *Memory trick*
> 
> **c**reate, e**x**tract, lis**t** · **z** = gzip · **f** = file name comes next

Single files:

```bash
gzip app.log          # creates app.log.gz and removes app.log
gunzip app.log.gz
zcat app.log.gz | grep ERROR   # read without extracting
```

---

# ⏯ 10. Job Control & History

```bash
sleep 300            # start something long
# Ctrl + Z           → suspend it
jobs                 # list jobs
bg %1                # resume job 1 in the background
fg %1                # bring it back to the foreground
kill %1              # stop it
```

History:

```bash
history              # numbered list
history | grep tar   # find that command you ran last week
!42                  # run command number 42 again
```

---

# In the next session ...

All of this becomes **scripts**:

- Variables, conditions and loops
- Arguments and exit codes
- Scheduling them with `crontab`
