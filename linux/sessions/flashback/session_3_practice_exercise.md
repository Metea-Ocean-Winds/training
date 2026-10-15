# 🧪 Session 3 – Practice Exercise

**Course:** Linux – Flashback & Shell Power-Ups  
**Files Provided:** `app.log`, `process.log`  
**Tools Allowed:** everything from Sessions 1–3

---

# 🧭 Instructions

- Work in a new folder: `mkdir -p ~/session3 && cd ~/session3`
- Copy the logs into it before starting.
- Use ONLY command line tools.
- Write down every command you use in a file called `commands.txt` (hint: `history`).

---

# 🔁 Part 1 – Flashback

1. Count the `ERROR` lines in `app.log`.

2. Show the 5 most frequent IP addresses with their count.

3. Show the lines of `process.log` where `STATUS=DEGRADED` and the process is `cache`.

4. Replace `ERROR` with `ALERT` in the output stream (do not modify the file).

5. Find every `.log` file under your home directory, hiding permission errors.

---

# 💲 Part 2 – Variables & Substitution

1. Store today's date (`YYYY-MM-DD`) in a variable called `today`.

2. Store the number of `WARNING` lines in a variable called `warnings`.

3. Print exactly this sentence using both variables:
   
   `On 2026-10-15 there were 123 warnings`

4. Print the same sentence with single quotes. What happens? Why?

5. Show each folder of your `PATH` on its own line.

---

# 📁 Part 3 – Wildcards & Braces

1. With ONE command, create the folders `reports/daily`, `reports/weekly` and `reports/monthly`.

2. With ONE command, create the files `day1.txt` … `day7.txt` inside `reports/daily`.

3. List only `day2.txt`, `day3.txt` and `day4.txt` using a wildcard range.

4. Make a backup copy of `app.log` called `app.log.bak` using brace expansion.

---

# 🚦 Part 4 – Exit Codes

1. Run `grep -q CRITICAL app.log`. What is the exit code? Why?

2. Write a one-liner that prints `Errors found` if `app.log` contains `ERROR`, and `All clean` otherwise.

3. Write a one-liner that creates `archive/` and moves `app.log.bak` into it, **only if** the folder was created successfully.

4. What is the difference between these two lines?
   
   ```bash
   cd /does/not/exist; rm -f *.txt
   cd /does/not/exist && rm -f *.txt
   ```

---

# 🛠 Part 5 – tr, tee, diff

1. Print all log levels of `app.log` in lowercase.

2. Extract the CPU values from `process.log` as plain numbers (no `CPU=` and no `%`).

3. Save all `ERROR` lines into `errors.txt` **and** show how many there are, using a single pipeline.

4. Create `app_redacted.log` where every IP address is replaced by `x.x.x.x`. Compare it with `app.log` using `diff` and show only the first 10 lines of the difference.

---

# 📦 Part 6 – Archives

1. Create `logs_backup.tar.gz` containing both log files.

2. List the content of the archive without extracting it.

3. Extract the archive into a folder called `restore/`.

4. Compress `errors.txt` with `gzip`, then count its `ERROR` lines without decompressing it.

---

# ⏯ Part 7 – Jobs

1. Start `sleep 600`, suspend it, and send it to the background.

2. Start a second `sleep 900 &`.

3. List your jobs, bring the first one back to the foreground, and stop it with `Ctrl + C`.

4. Kill the remaining job using its job number.

---

# 🏆 Final Challenge

Produce a file named `summary_<today>.txt` (use your `today` variable) that contains:

1. The date
2. The number of lines in each log
3. The top 3 endpoints in `app.log`
4. The process with the highest single CPU value in `process.log`

Then archive `summary_<today>.txt` together with `errors.txt.gz` into `session3_<today>.tar.gz`.

> *Hint*: This is the kind of task you will automate with a script in Session 4.
