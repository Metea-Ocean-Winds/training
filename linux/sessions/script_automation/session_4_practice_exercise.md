# 🧪 Session 4 – Practice Exercise

**Course:** Linux – Bash Scripting  
**Files Provided:** `app.log`, `process.log`  
**Tools Allowed:** everything from Sessions 1–4

---

# 🧭 Instructions

- Work in `~/session4`. Put your scripts in `~/bin`.
- Every script must start with `#!/bin/bash`.
- Every script must be executable (`chmod +x`).
- Run `shellcheck` on every script before calling it finished.

---

# 👋 Part 1 – Warm-up Scripts

1. Write `sysinfo.sh` that prints:
   - your user name
   - the host name
   - the current date and time
   - how long the machine has been running (`uptime -p`)

2. Write `greet.sh` that asks for a name with `read` and greets that person. If the name is empty, print `Hello, stranger`.

3. Write `count_lines.sh` that receives **any number** of files as arguments and prints the number of lines of each one.
   
   ```bash
   ./count_lines.sh app.log process.log
   app.log: 1000
   process.log: 1000
   ```

---

# 🔀 Part 2 – Conditions

Write `check_file.sh <path>` that prints:

- `Usage: check_file.sh <path>` and exits with code `1` when no argument is given
- `<path> does not exist` and exits with code `2` when the path doesn't exist
- `<path> is a directory` for directories
- `<path> is an empty file` for empty files
- `<path> is a file with N lines` otherwise

Test every branch. Check the exit code each time with `echo $?`.

---

# 🔁 Part 3 – Loops

1. Write `levels.sh` that prints the count of each log level in `app.log` using a `for` loop over `ERROR WARNING INFO DEBUG`.

2. Write `cpu_alert.sh` that reads `process.log` line by line with `while read` and prints an alert for every line with CPU above a threshold given as the first argument (default `80`).
   
   ```bash
   ./cpu_alert.sh 90
   ALERT 08:12:44 api-service CPU=93%
   ```

3. Write `rename_logs.sh` that adds today's date as a prefix to every `.log` file in a folder given as argument (`app.log` → `2026-10-15_app.log`). Test it on a **copy** of the files!

---

# 🏆 Part 4 – Main Challenge: `log_report.sh`

Remember the **Incident Report** from Session 2? You built it by hand. Now automate it.

```bash
log_report.sh <app_log> <process_log> [output_dir]
```

Requirements:

1. Validate that both log files exist and are readable. Otherwise print an error to stderr (`>&2`) and exit with a non-zero code.

2. `output_dir` is optional. Default: the current directory. Create it if it doesn't exist.

3. The output file name must contain a timestamp:
   
   `incident_report_YYYY-MM-DD_HHMM.txt`

4. The report must contain:
   - Report date and the analysed files
   - Total number of `ERROR` entries
   - Top 3 most frequent IP addresses
   - Most frequent HTTP status code
   - Number of high CPU events (> 80%)

5. Use at least **two functions** (for example `log` and `top_ips`).

6. Update a symbolic link `latest_incident` in `output_dir` pointing to the newest report.

7. Exit with code `0` on success.

Example run:

```bash
log_report.sh ~/session4/app.log ~/session4/process.log ~/reports
[10:15:02] Analysing /home/alice/session4/app.log
[10:15:02] Report written to /home/alice/reports/incident_report_2026-10-15_1015.txt
```

---

# ⏰ Part 5 – Schedule It

1. Add a crontab entry that runs `log_report.sh` **every 5 minutes**, writing reports into `~/reports` and its own output into `~/reports/cron.log`.

2. Wait 10 minutes. Check that new reports appear and `latest_incident` follows the newest one.

3. Check `~/reports/cron.log`. Is it empty? Should it be?

4. Change the schedule to **every weekday at 07:30**.

5. Verify with `crontab -l`.

---

# 🧠 Bonus – Backup with Rotation

Write `backup.sh <source_dir> <backup_dir>` that:

1. Creates `backup_YYYY-MM-DD_HHMMSS.tar.gz` of `source_dir` inside `backup_dir`
2. Keeps only the **5 most recent** backups and deletes older ones
3. Prints how much space the backup folder uses (`du -sh`)

> *Hint*: `ls -1t backup_*.tar.gz | tail -n +6` lists everything except the newest 5.

Schedule it once a day at 02:00.

---

# 🧹 Cleanup

When finished, remove your test cron jobs:

```bash
crontab -e     # delete the lines you added
crontab -l     # confirm
```
