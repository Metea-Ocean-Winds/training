# Linux Command Line Cheat Sheet

---

# Shortcuts

| **Category**   | **Shortcut** | **Action / Function**                                     |
| -------------- | ------------ | --------------------------------------------------------- |
| **Navigation** | **Tab**      | **Autocomplete** commands, paths, and filenames           |
|                | **Ctrl + A** | Move cursor to the **beginning** of the line              |
|                | **Ctrl + E** | Move cursor to the **end** of the line                    |
|                | **Alt + B**  | Move cursor back **one word**                             |
|                | **Alt + F**  | Move cursor forward **one word**                          |
| **Editing**    | **Ctrl + W** | **Cut the word** before the cursor                        |
|                | **Ctrl + U** | **Cut everything** from cursor to start of line           |
|                | **Ctrl + K** | **Cut everything** from cursor to end of line             |
|                | **Ctrl + Y** | **Paste** (Yank) the last cut text                        |
|                | **Ctrl + _** | **Undo** the last editing change                          |
|                | **Alt + T**  | Swap the current word with the previous one               |
| **History**    | **Ctrl + R** | **Search history** (type to find previous commands)       |
|                | **!!**       | Repeat the **entire last command**                        |
|                | **!$**       | Insert the **last argument** of the previous command      |
|                | **Alt + .**  | Cycle through the **last arguments** of previous commands |
| **Control**    | **Ctrl + C** | **Kill/Interrupt** the current process                    |
|                | **Ctrl + Z** | **Suspend** (pause) the current process                   |
|                | **Ctrl + L** | **Clear** the screen (same as `clear` command)            |
|                | **Ctrl + D** | **Exit** the current shell or log out                     |
|                | **Ctrl + S** | **Freeze** terminal output (Stop scrolling)               |
|                | **Ctrl + Q** | **Unfreeze** terminal output (Resume scrolling)           |

## Navigation

```bash
pwd              # Show current directory
ls               # List files
ls -la           # List including hidden files
cd folder        # Enter folder
cd ..            # Go up one level
cd ~             # Go to home directory
```

---

## Text Inspection

```bash
cat file.txt        # Print entire file
head file.txt       # Show first 10 lines
head -n 20 file.txt # Show first 20 lines
tail file.txt       # Show last 10 lines
tail -f file.txt    # Follow file updates
more file.txt       # View file page by page
```

---

## File Management

```bash
mkdir folder     # Create directory
touch file.txt   # Create empty file
cp a b           # Copy file
mv a b           # Move or rename
rm file.txt      # Delete file
rm -r folder     # Delete directory
```

---

## Search (find)

```bash
find . -name "notes.txt"               # Starting from here (the dot and apply recurisive search
find . -iname "notes.txt"              # This will find "Notes.txt", "NOTES.txt", etc
find /home -name "*.jpg"               # This finds all JPG files in the home directory
find . -type d                         # find directories only
find . -type f                         # find files only
find / -size +100M                     # finding larger than 100Mb
find . -size -10k                      # finding smaller than 10kb
find . -mtime -1                       # finding in the last 24 hours
find . -mtime +30                      # finding more than 30 days ago
find . -name "*.tmp" -delete           # delete all .tmp files
find . -type f -exec chmod 644 {} \;   # change permissions. Note: The {} is a placeholder for the file found, and \; tells Linux the command is finished.
```

Add `2>/dev/null` to the end to hide "Permission Denied" errors

---

## Search (grep)

```bash
grep "text" file.txt          # Search inside file
grep -i "text" file.txt       # Ignore case
grep -n "text" file.txt       # Show line numbers where the mathc is found
grep -v "text" file.txt       # Invert match
grep -r "text" .              # Recursive search
grep -E "a|b" file.txt        # Extended regex (OR)
grep -c "text" file.txt       # Count matches
grep -w "is" file.txt         # Matches "is" but not "this" or "his"
```

---

## Transform Text (sed)

```bash
sed 's/old/new/' file.txt      # Replace first match per line
sed 's/old/new/g' file.txt     # Replace all matches per line
sed '/DEBUG/d' file.txt        # Delete lines matching DEBUG
sed -n '2p' file.txt           # Print only line 2
sed -n '/ERROR/p' file.txt     # Print only matching lines
```

---

## Extract Fields (awk)

```bash
awk '{print $1}' file.txt              # Print first field
awk '{print $1, $3}' file.txt          # Print fields 1 and 3
awk '$3 > 300 {print $0}' file.txt     # Print lines where field 3 > 300
awk -F: '{print $1}' /etc/passwd       # Use : as field separator
awk '{print $NF}' file.txt             # Print last field
```

---

## Cut (Simple Column Extraction)

```bash
cut -d' ' -f1 file.txt         # First column using space delimiter
cut -d: -f1 /etc/passwd        # First field before :
cut -c1-10 file.txt            # Characters 1 to 10
```

---

## Pipes & Redirection

```bash
|        # Pipe output to next command
>        # Redirect stdout (overwrite)
>>       # Redirect stdout (append)
2>       # Redirect stderr
2>>      # Append stderr
2>&1     # Redirect stderr to wherever stdout is going
```

Examples:

```bash
cat file.txt | sort | uniq -c | sort -nr
command > output.log 2>&1
```

---

## Sort / Uniq / Count

```bash
sort file.txt                  # Sort lines
sort -n numbers.txt             # Numeric sort
sort file.txt | uniq            # Unique lines
sort file.txt | uniq -c         # Count occurrences
sort file.txt | uniq -c | sort -nr  # Top occurrences
wc -l file.txt                  # Count lines
```

---

## Processes

```bash
ps
top
kill PID
Ctrl + C   # Stop running process
```

---

## Permissions

```bash
ls -l
chmod 755 file
chown user:group file
```

r = 4, w = 2, x = 1

---

## Networking

```bash
ping host
curl example.com
```

---

## Help

```bash
man command
history
```

---
