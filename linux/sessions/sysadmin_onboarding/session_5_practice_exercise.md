# 🧪 Session 5 – Practice Exercise

**Course:** Linux – System Administration Basics  
**Environment:** Your own training VM with `sudo`  
**Tools Allowed:** everything from Sessions 1–5

> ⚠️ This exercise creates users, groups and sudo rules. Do the **Cleanup** part at the end.

---

# 🧭 Scenario

A new data team joins the company. You are the administrator of their server.

The team:

| User    | Full name      | Role       |
| ------- | -------------- | ---------- |
| `ana`   | Ana Lopez      | Team lead  |
| `ben`   | Ben Carter     | Analyst    |
| `chloe` | Chloe Martin   | Analyst    |

---

# 👤 Part 1 – Users

1. Create the three users with a home folder, `/bin/bash` as shell and their full name as description.

2. Set a password for each of them.

3. Force `ben` and `chloe` to change their password at first login.

4. Show the `/etc/passwd` line of the three users using a single `grep -E`.

5. List all human users (UID ≥ 1000) with their UID and shell.

---

# 👥 Part 2 – Groups

1. Create the group `datateam`.

2. Add the three users to `datateam`.

3. Create the group `teamleads` and add only `ana`.

4. Verify the memberships with `id` and `getent group`.

5. Run `sudo usermod -G datateam ana` **without** `-a` on purpose. What happened to `teamleads`? Fix it.

---

# 📁 Part 3 – Shared Folder

1. Create `/srv/datateam` owned by `root` and group `datateam`.

2. Set permissions so that:
   - members of `datateam` can read, write and enter
   - nobody else can do anything
   - new files automatically belong to group `datateam`

3. As `ben`, create a file in the folder. As `chloe`, check its group and try to edit it.

4. Add the sticky bit. As `chloe`, try to delete `ben`'s file. What happens now?

5. As your own user (not in `datateam`), try to `ls /srv/datateam`. Explain the result.

---

# 📜 Part 4 – Sudoers

1. Using `visudo`, create `/etc/sudoers.d/teamleads` so that members of `teamleads` can:
   - read system logs with `journalctl`
   - restart the cron service with `systemctl restart cron`
   
   …and nothing else.

2. Validate the configuration with `visudo -c`.

3. As `ana`, list her sudo rights and restart cron.

4. As `ana`, try `sudo apt update`. What happens? Where is that attempt logged?

5. As `ben`, try `sudo -l`. What is the result?

---

# 💽 Part 5 – Disk Inspection

Answer using commands only:

1. How many disks does the VM have? What are their device names?

2. Which partition is mounted on `/`? What filesystem type does it use?

3. What is the UUID of the root partition? Find it in `/etc/fstab`.

4. Is the partition table MBR (`dos`) or GPT?

5. How much free space is left on `/`?

6. Which 5 folders under `/var` use the most space?

7. Is there any swap? How big?

---

# 🔗 Part 6 – Mounting

1. Create `/mnt/scratch` and mount a 100 MB `tmpfs` on it.

2. Verify it with `df -h` and `findmnt`.

3. Give `datateam` write access to it. As `ben`, create a file in it.

4. Open a second terminal, `cd /mnt/scratch` there, and try to unmount from the first terminal. Find out who is blocking it.

5. Unmount it successfully. Is the file still there?

6. **Theory**: write down the `/etc/fstab` line that would mount this `tmpfs` at every boot. Do **not** add it.

---

# 🏆 Final Challenge – `audit_report.sh`

Using what you learned in Session 4, write `audit_report.sh` that must be run with `sudo` and produces `audit_<hostname>_<YYYY-MM-DD>.txt` containing:

1. Hostname, date and uptime
2. Human users (UID ≥ 1000) with their shell and groups
3. Members of the `sudo` group
4. Content of every file in `/etc/sudoers.d/` (skip `README`)
5. Disks and partitions (`lsblk -f`)
6. Usage of every mounted real filesystem (`df -hT -x tmpfs -x squashfs -x devtmpfs`)
7. A **WARNING** line for every filesystem above 80 % usage

Requirements:

- Exit with an error if not run as root (hint: `$EUID` or `id -u`)
- Use at least one function and one loop
- Pass `shellcheck` without warnings

---

# 🧹 Cleanup

Undo everything you created:

```bash
sudo umount /mnt/scratch 2>/dev/null; sudo rmdir /mnt/scratch
sudo rm /etc/sudoers.d/teamleads
sudo visudo -c
sudo userdel -r ana
sudo userdel -r ben
sudo userdel -r chloe
sudo groupdel teamleads
sudo groupdel datateam
sudo rm -r /srv/datateam
```

Verify:

```bash
getent passwd ana ben chloe
getent group datateam teamleads
ls /etc/sudoers.d
findmnt /mnt/scratch
```

All four commands should return nothing (except `README` in `/etc/sudoers.d`).
