# .bashrc and Aliases Guide

## What is .bashrc?

`.bashrc` is a configuration file executed every time you open a new terminal session.

It is used to:
- Define aliases
- Set environment variables
- Customize your shell

---

# Open .bashrc

```bash
nano ~/.bashrc
```

---

# Creating Aliases

Syntax:

```bash
alias name='command'
```

Examples:

```bash
alias ll='ls -la'
alias gs='git status'
alias update='sudo apt update && sudo apt upgrade'
```

---

# Apply Changes

After saving `.bashrc`:

```bash
source ~/.bashrc
```

Or reopen the terminal.

---

# Best Practices

- Keep aliases short and meaningful
- Avoid overwriting important system commands
- Comment your aliases

Example with comment:

```bash
# List all files in long format
alias ll='ls -la'
```

---

Aliases save time and reduce typing errors.

