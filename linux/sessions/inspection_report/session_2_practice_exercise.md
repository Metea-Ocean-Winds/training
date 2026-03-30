# 🧪 Session 2 – Practice Exercise

**Course:** Linux – Command Line Wizard  
**Files Provided:** `app.log`, `process.log`  
**Tools Allowed:** grep, sed, awk, sort, uniq, wc, head, tail, loops, wildcards (*), redirection (> >>), ln

---

# 🧭 Instructions

- Use ONLY command line tools.
- Do NOT open the files in an editor unless explicitly required.
- Think in pipelines.
- Build results step by step.
- When asked to create files, construct them intentionally using `>` and `>>`.

---

# 🔎 Part 1 – File Inspection

1. How many lines are in `app.log`?

2. How many lines are in `process.log`?

3. Show the first 5 lines of `app.log`.

4. Show the last 10 lines of `process.log`.

5. If `app.log` were growing, how would you monitor it live?

---

# 📊 Part 2 – Log Level Analysis (app.log)

1. How many `ERROR` entries are there?

2. How many `WARNING` entries are there?

3. How many `INFO` entries are there?

4. Create a ranked list of all log levels sorted by frequency.

---

# 🌐 Part 3 – IP Address Investigation

1. Extract all IP addresses from `app.log`.

2. How many unique IP addresses appear?

3. What are the top 5 most frequent IP addresses?

4. Save the result into a file called:
   
   `ip_report.txt`

---

# 📈 Part 4 – HTTP Status Codes

1. Extract all HTTP status codes.

2. How many responses returned status `200`?

3. How many returned `500`?

4. Sort all status codes numerically.

5. Which status code appears most frequently?

---

# ⚙️ Part 5 – Process Log Analysis (process.log)

1. Extract only the CPU values.

2. Show processes where CPU usage is greater than 70%.

3. Count how many times CPU exceeded 80%.

4. Extract unique process names.

---

# 🔁 Part 6 – Multi-File Investigation

Using BOTH log files:

1. Count total `ERROR` entries across both logs.

2. Count total lines across both logs combined.

3. List unique IP addresses appearing in either file.

---

# 🛠 Part 7 – Stream Transformation

1. Replace all IP addresses in `app.log` with `REDACTED` (stream only, do not modify original file).

2. Remove all `DEBUG` lines (stream only).

3. Save a cleaned version of the file as:
   
   `app_clean.log`

---

# 🏆 Final Challenge – Incident Report

You are investigating a production issue.

Create a file named:

`incident_report.txt`

It must contain:

1. Total number of `ERROR` entries
2. Top 3 most frequent IP addresses
3. Most frequent HTTP status code
4. Number of high CPU events (>80%) from `process.log`

Build the file step by step using:

`>` to create  
`>>` to append

Finally, create a symbolic link:

`latest_incident` → `incident_report.txt`

---

# 🧠 Bonus

Analyse all the process that are running with `ps aux` and through pipes, identify interesting processes you would like to know which user started and when.

Then sort them by CPU usage, but just keeping the top 10.

Could you kill those which were initiated by a non-admin user that have been running beyond a "reasonable"" time
