# Crontab Guide

## What is cron?

Cron is a job scheduler in Linux.
It runs commands automatically at specified times.

---

# Edit Your Crontab

```bash
crontab -e
```

This opens your personal cron configuration.

---

# Crontab Format

```
* * * * * command
│ │ │ │ │
│ │ │ │ └── Day of week (0-7)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
```

---

# Examples

Run every day at 2:30 AM:

```
30 2 * * * /home/user/script.sh
```

Run every 5 minutes:

```
*/5 * * * * /home/user/script.sh
```

---

# View Existing Jobs

```bash
crontab -l
```

---

# Remove Crontab

```bash
crontab -r
```

---

# Best Practices

- Always use absolute paths
- Redirect output to a log file

Example:

```
0 1 * * * /home/user/backup.sh >> /home/user/backup.log 2>&1
```

Cron is powerful for automation and DevOps workflows.

