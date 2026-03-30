# Nano Editor Guide

Nano is a simple terminal text editor, is beginner-friendly and ideal for quick edits.

Open a file:

```bash
nano file.txt
```

If the file does not exist, nano will create it.

---

# Basic Controls

Nano uses CTRL shortcuts.

Notation:
^ means CTRL

Examples:

- ^O  → Write (save)
- ^X  → Exit
- ^K  → Cut line
- ^U  → Paste line
- ^W  → Search
- ^G  → Help

---

# Saving a File

1. Press CTRL + O
2. Press Enter to confirm filename
3. Press CTRL + X to exit

---

# Editing .bashrc

Open:

```bash
nano ~/.bashrc
```

After editing, reload configuration:

```bash
source ~/.bashrc
```

---

# Change the default editor

Add this line to your `~/.bashrc`

```bash
export VISUAL=nano
export EDITOR=nano
```

Then reload:

```bash
source ~/.bashrc
```

This will make nano the default editor in your crontab.
