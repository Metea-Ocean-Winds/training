# 🧙 Session 2 – Command Line Wizard

**Duration:** 90 minutes  

**Theme:** Transform data like a professional

---

# 🎯 Objectives

By the end of this session you should be able to:

- Use `find` `grep`, `sed`, `cut` and `awk` confidently
- Work across multiple files using `*`
- Analyse logs using `sort`, `uniq`, and `wc`
- Use `head` and `tail` efficiently
- Use `>` and `>>` intentionally
- Create and understand symbolic links

---

# find

`find` allows you to search through thousands of files using specific criteria like size, date, or permissions.

The basic syntax for the command is: `find [where to look] [criteria] [what to do]`

***Finding by name***

```bash
find . -name "notes.txt"  # Starting from here (the dot) and apply recurisive search
find . -iname "notes.txt" # This will find "Notes.txt", "NOTES.txt", etc
find /home -name "*.jpg"  # This finds all JPG files in the home directory
```

***Finding by File Type***

```bash
find . -type d   # find directories only
find . -type f   # find files only
```

***Finding by size***

```bash
find / -size +100M   # finding larger than 100Mb
find . -size -10k    # finding smaller than 10kb
```

***Finding by time***

```bash
find . -mtime -1   # finding in the last 24 hours
find . -mtime +30  # finding more than 30 days ago
```

***Doing Something with the Results***

```bash
find . -name "*.tmp" -delete           # delete all .tmp files
find . -type f -exec chmod 644 {} \;   # change permissions. Note: The {} is a placeholder for the file found, and \; tells Linux the command is finished.
```

***Pro tip***

Add `2>/dev/null` to the end to hide "Permission Denied" errors 

---

# 🔎 2. grep – Pattern Search

The name stands for **G**lobal **R**egular **E**xpression **P**rint. In plain English: it searches for a specific string of text and shows you every line where it appears.

***Basic search***

```bash
grep "ERROR" file.txt
```

***Useful flags***

```bash
grep -i "error" file.txt     # ignore case
grep -n "ERROR" file.txt     # show line numbers
grep -v "INFO" file.txt      # invert match
grep -E "ERROR|WARNING" file.txt
grep -c "ERROR" file.txt     # count matches
grep -r "ERROR" .           # recursive search
```

> *Trick for large outputs*
> 
> Use the pipeline and `more` to go though all the lines page by page

```bash
grep -r "ERROR" .  | more # press <ENTER> for more, and q to Quit
```

***Multiple files***

```bash
grep "ERROR" *.log
```

***Count across all logs***

```bash
grep -h "ERROR" *.log | wc -l
```

---

# ✏ 3. sed – Stream Editing

It stands for **S**tream **ED**itor. It is used to transform or filter text as it flows through a pipeline. Its most famous trick is "search and replace," but it can do much more.

The basic syntax is: `sed [options] 'command' [file]`

***Replace text***

```bash
sed 's/error/ERROR/' file.txt   # Replace the first occurrence on each line:
sed 's/error/ERROR/g' file.txt  # Replace ALL occurrences on each line (Global)
sed 's/old/new/gi' file.txt     # Case-insensitive replace
```

***Delete lines***

```bash
sed '/DEBUG/d' file.txt    # Delete lines matching
sed '$d' file.txt          # Delete the last line
sed '3d' file.txt          # Delete line 3
```

***Print matching lines <u>only</u>***

```bash
sed -n '/ERROR/p' file.txt    
```

***Print specific lines <u>only</u>***

The `-n` flag tells `sed `not to print everything by default, and `p` tells it to print only the matches.

```bash
sed -n '5p' file.txt         # line 5
sed -n '1,3p' file.txt      # lines 1 to 3
```

***Saving your changes***

By default, `sed` just prints the result to your screen (`stdout`). It doesn't change the original file.

```bash
sed -i 's/old/new/g' file.txt      # Edit the file in-place
sed -i.bak 's/old/new/g' file.txt  # Edit in-place with a backup (This creates file.txt.bak just in case!)
```

---

# 📊4. Cut - column processing

`cut` is a simple, lightweight tool. It’s perfect when your data is neatly separated by a single character (like a comma or a tab).

**Basic Syntax:** `cut [options] [file]`

```bash
cut -c 1-10 file.txt           # Extracts the first 10 characters of every line
cut -d "," -f 2 file.csv       # -d tells the separator -f tell the column number
cut -d ":" -f 1,3 /etc/passwd  # Extracts columns 1 and 3
```

---

# 📊 5. awk – Field Processing

`awk` is much more powerful than `cut`. It is actually a full programming language designed for text processing.

Beginners love it because it handles **irregular spacing** (like multiple spaces or tabs) automatically.

***Print first column***

```bash
awk '{print $1}' file.txt
```

***Print multiple columns***

```bash
awk '{print $1, $3}' file.txt
```

***Conditional***

```bash
awk '$6 == 200 {print $0}' file.txt  # {print $0} prints the whole line

# WARNING
awk '$6 = 200 {print $0}' file.txt # THIS WILL ASSIGN TO THE 7th FIELD 200, AND ALL THE LINES WILL BE PRINTED

# Compare
awk '$6 == 200 {print $0}' file.txt 
awk '$6 = 200 {print $0}' file.txt
```

***Custom separator***

```bash
awk -F: '{print $2}' file.txt
awk -F: '$2 == 400 {print $0}' file.txt
```

***Print a given line***

```bash
awk 'NR==1'   # NR stands for Number of Record; this prints only the first line.
```

***Last field***

```bash
awk '{print $NF}' file.txt
```

---

# 🧠 6. Thinking in Streams

## Pipelines

Linux commands work with text streams:

- **stdin** → input
- **stdout** → output
- **stderr** → errors

Mental model:

file → command → command → command → result

Example:

```bash
cat file.txt | grep ERROR | sort | uniq -c | sort -nr
```

Each command transforms the data.

## xargs

Think of combining find and grep.

Find all `.conf` files and search them for the word "Port".

Have you though about this solution?

```bash
find . -name "*.conf" | grep "Port"
```

the pipe (`|`) sends the *filenames* to `grep` as plain text. `grep` will then search that text for the word "Port". It won't actually open the files; it will just look at the list of names you gave it!

***The solution is using `xargs`***

```bash
find . -name "*.conf" | xargs grep "Port"
```

`xargs` acts as a **translator**. it takes the lines of text coming out of the pipe and turns them into actual arguments for the next command.

- **Without `xargs`:** `grep` searches the *words* produced by `find`.

- **With `xargs`:** `grep` opens the *files* named by `find`.

---

# 🔢 7. sort, uniq, wc

Sort lines:

```bash
sort file.txt
```

Remove duplicates:

```bash
sort file.txt | uniq
```

Count occurrences:

```bash
sort file.txt | uniq -c
```

Sort by frequency:

```bash
sort file.txt | uniq -c | sort -nr
```

Count lines:

```bash
wc -l file.txt
```

---

# 👀 8. Processes

***Checking Processes***

To see what is happening on your system, use these two commands:

- **`ps` (Process Status):** Provides a "snapshot" of current processes. Usually used as `ps aux` to see every process running on the system.

- **`top` or `htop`:** These provide a **real-time**, interactive list. While `top` is the standard, `htop` is much more user-friendly with color-coded bars for CPU and RAM usage.

***Managing Processes***

If a program freezes or you need to clear resources, you "kill" the process using its **PID** (Process ID):

- **`kill <PID>`:** Sends a polite request for the program to stop.

- **`kill -9 <PID>`:** The "force quit" option. It stops the process immediately without letting it save data.

***The Power Duo***

Normally, if you start a long task in the terminal and then close the window or log out, that task dies instantly. This is where `nohup` (No Hang Up) and `&` (Background) come in.

How it works? When you combine them, you create a "fire and forget" command:

```bash
nohup ./long_script.sh &
```

- **`&` (The Backgrounder):** This lets you keep using your terminal while the script runs in the back.

- **`nohup` (The Shield):** This ensures the script keeps running even if you close the terminal or lose your internet connection. **(it disconnects the command from your session PID**)

- **The Output:** By default, any messages the script would have printed to your screen get saved into a file called `nohup.out`.

---

# 📤 9. Redirection

Overwrite file:

```bash
command > output.txt
```

Append to file:

```bash
command >> output.txt
```

Redirect both output and errors:

```bash
command > output.log 2>&1
nohup ./long_script.sh > output.log 2>&1 &
```

---

# 🔗 10. Symbolic Links

Create link:

```bash
ln -s report.txt latest_report
```

Check link:

```bash
ls -l
```

You will see:

latest_report -> report.txt

---

# In the intermediate course ...

- Scripting

- Scheduling process `crontab`

# In the administrator course ...

- Create users

- SSH connection

- Orchestra process