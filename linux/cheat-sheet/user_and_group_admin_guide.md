# Users, Groups & sudo Guide

---

# Key Files

| File                | Content                                  |
| ------------------- | ---------------------------------------- |
| `/etc/passwd`       | Users: `name:x:UID:GID:desc:home:shell`  |
| `/etc/shadow`       | Password hashes (root only)              |
| `/etc/group`        | Groups: `name:x:GID:members`             |
| `/etc/sudoers`      | sudo rules (edit with `visudo` only)     |
| `/etc/sudoers.d/`   | Drop-in sudo rules                       |
| `/var/log/auth.log` | Logins and sudo usage                    |

UID `0` = root · `1–999` = system · `1000+` = humans

---

# Identity

```bash
whoami                 # current user
id                     # UID, GID, groups
id alice               # another user
groups alice           # alice's groups
who                    # logged in users
last | head            # recent logins
getent passwd alice    # user entry
getent group sudo      # group entry and members
```

---

# Switching User

```bash
sudo command           # run one command as root
sudo -i                # root shell
su - alice             # become alice (her password)
sudo su - alice        # become alice (your sudo rights)
exit                   # go back
```

---

# Users

```bash
sudo adduser bob                              # interactive (Debian/Ubuntu)
sudo useradd -m -s /bin/bash -c "Bob" bob     # scriptable
sudo passwd bob                               # set password
sudo passwd -e bob                            # expire: change at next login
sudo usermod -c "Bob B." bob                  # change description
sudo usermod -s /bin/zsh bob                  # change shell
sudo usermod -L bob                           # lock
sudo usermod -U bob                           # unlock
sudo userdel bob                              # delete, keep home
sudo userdel -r bob                           # delete with home
```

---

# Groups

```bash
sudo groupadd team                # create
sudo usermod -aG team bob         # add bob (-a = APPEND!)
sudo gpasswd -d bob team          # remove bob
sudo groupdel team                # delete
```

⚠️ `usermod -G` without `-a` **replaces** all secondary groups.

Membership changes apply at next login.

---

# Special Permissions

| Bit      | Octal | Symbolic    | On a directory                         |
| -------- | ----- | ----------- | -------------------------------------- |
| setuid   | `4`   | `u+s`       | (files only) run as file owner         |
| setgid   | `2`   | `g+s`       | New files inherit the directory group  |
| sticky   | `1`   | `o+t`       | Only owners can delete their files     |

```bash
sudo chgrp team /srv/team
sudo chmod 2770 /srv/team      # rwxrws---  shared team folder
sudo chmod +t /srv/team        # add sticky bit
```

---

# sudoers

```bash
sudo visudo                              # edit main file
sudo visudo -f /etc/sudoers.d/team       # edit drop-in
sudo visudo -c                           # validate
sudo -l                                  # my rights
sudo -l -U alice                         # alice's rights
```

***Syntax***

```
who     where=(as_whom)   [NOPASSWD:] commands
alice   ALL=(ALL:ALL)     ALL
%team   ALL=(root)        /usr/bin/journalctl, /usr/bin/systemctl restart cron
deploy  ALL=(root)        NOPASSWD: /usr/bin/systemctl restart myapp
```

- `%` = group
- Use full command paths (`which cmd`)
- Drop-in file names: no `.` and no `~`
- Ubuntu: members of group `sudo` are full admins
