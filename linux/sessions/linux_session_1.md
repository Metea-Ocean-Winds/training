# Session 1 – What is Linux?

<img src="../images/Tux.svg.png" title="" alt="" width="461">

---

# 1. Introduction

## Objectives

By the end of this session, learners will:

- Understand what Linux is
- Understand what a distribution is
- Use basic terminal commands
- Navigate the filesystem

---

# 2. What is Linux?

## Simple Definition

When people hear *Linux*, they often imagine something complicated, hacker-like, or very technical.

So let’s simplify it.

At its core, **Linux is an operating system** — just like Windows or macOS.

An operating system is simply the layer of software that sits between you and the hardware.

It manages memory, CPU, storage, networking, and lets you run programs.

Without it, your computer is just a powered piece of metal.

## A Bit of History: UNIX

To really understand Linux, we need to step back in time.

In the 1970s, there was an operating system called **UNIX**.

UNIX was powerful, stable, and designed for multi-user, networked systems.  
It became extremely influential in universities, research labs, and later enterprise systems.

But there was one problem:

It was proprietary and expensive.

Over time, many systems were inspired by UNIX, copying its philosophy and design.

Linux is one of them.

Linux was created in 1991 by Linus Torvalds as a UNIX-like system — meaning:

It follows the same design philosophy:

- Small tools that do one thing well

- Everything is a file

- Strong command-line culture

- Multi-user from the beginning

So when you use Linux, you’re actually using a modern, open-source descendant of the UNIX tradition.

## What About macOS?

Here’s something many people don’t realize:

macOS is also UNIX-based.

Under the hood, macOS uses a UNIX-certified core called Darwin.

That’s why:

- The terminal on macOS looks familiar

- Many Linux commands work the same way

- Tools like `ls`, `grep`, `cat`, `ssh` behave almost identically

If someone is comfortable in the macOS terminal, they already understand a big part of Linux.

The difference is mainly:

- Linux is fully open source

- macOS includes Apple’s proprietary layers and interface

But philosophically, they’re cousins.

If Windows is one branch of the operating system family tree, Linux and macOS share a different branch — the UNIX branch.

## So What Makes Linux Special?

It is:

- Open source
- Free to use
- Highly customizable
- Dominant in servers and cloud systems

#### Where Is Linux Used?

Let’s put it into context.

Most of the internet runs on Linux.

Web servers?  Linux.

Cloud platforms like AWS, Azure, GCP? Mostly Linux under the hood.

DevOps environments and CI/CD pipelines?  Linux.

Containers like Docker?  Linux kernel features.

Embedded systems?  Routers, smart TVs, IoT devices — often Linux.

And even Android phones use the Linux kernel.

**So even if you’ve never used Linux directly, you are interacting with it constantly.**

## The Kernel vs The Distribution

One important clarification:

Linux technically refers to the **kernel** — the core engine.

What you install — like Ubuntu or Fedora — is called a **distribution**.

A distribution packages:

- The Linux kernel

- System tools

- A desktop environment (optional)

- Preconfigured software

So Linux is the engine.  
Ubuntu is the car built around that engine.

## Why Should You Care?

If you’re:

- A developer

- A system administrator

- Working in cloud

- Interested in cybersecurity

- Or even just curious about how computers really work

Linux matters.

It’s not just another operating system.

It’s the foundation of modern infrastructure.

And learning Linux — especially the command line — gives you direct access to how systems really behave.

You stop being just a user.

You start understanding the machine.

## Transition to the Terminal

And that’s why we’re going to spend time in the terminal.

Because Linux was designed to be controlled through text.

The command line is not old-fashioned.

It’s powerful.

And by the end of today, it won’t feel scary anymore.

It will feel logical.

---

# 3. Key Concepts

Now that we understand where Linux comes from, let’s break down a few key ideas.

These are words you’ll hear all the time:

- Kernel

- Distribution

- Terminal

- Shell

If you understand these four, Linux suddenly makes sense.

## Kernel

Let’s start with the **kernel**. The kernel is the core of the operating system.

If the operating system were a city, the kernel would be the infrastructure — the roads, electricity grid, water system.

It’s the part that talks directly to the hardware.

When you:

- Save a file

- Connect to Wi-Fi

- Allocate memory

- Run a program

You are not talking to the hardware directly. The kernel is.

It manages:

- CPU scheduling

- Memory allocation

- Device drivers

- Disk access

- Networking

In Linux, the kernel is called — quite literally — the Linux kernel.

Everything else sits on top of it.

So when we say “Linux”, technically we’re often referring to the kernel itself.

#### Distribution (Distro)

Now here’s where beginners often get confused.

If Linux is the kernel… what is Ubuntu? Ubuntu is not “Linux” in the strict sense. Ubuntu is a **distribution**.

A distribution — or “distro” — is a complete packaged operating system built around the Linux kernel.

It includes:

- The Linux kernel

- System utilities

- A package manager

- A desktop environment (if graphical)

- Preinstalled software

Think of it like this:

The kernel is the engine.  A distribution is the full car.

Different distros are like different car brands — they use the same engine architecture but make different design decisions.

For example:

- Ubuntu – beginner-friendly, popular, strong community

- Debian – stable and conservative

- Fedora – cutting-edge and developer-focused

Underneath, they all use the Linux kernel.

But the experience, defaults, and tools may differ.

#### Terminal

Now let’s talk about the **terminal**.

The terminal is simply a text-based interface.

Instead of clicking icons and menus, you type commands.

It may look old-fashioned.

But it’s extremely powerful.

Why?

Because:

- It’s precise

- It’s scriptable

- It’s fast

- It works remotely

- It requires almost no system resources

Most serious server environments don’t even have a graphical interface.

They run purely through the terminal.

When you open a terminal, you’re opening a doorway into direct system interaction.

## Shell

Inside the terminal, something is listening to you.

That something is the **shell**.

The shell is the program that interprets your commands.

When you type:

`ls`

The shell:

1. Reads what you typed

2. Finds the program called `ls`

3. Executes it

4. Displays the result

The most common Linux shell is **bash**.

There are others:

- zsh

- fish

- sh

But bash is the classic and most widely used.

So to summarize:

- The **kernel** talks to hardware.

- The **distribution** packages everything together.

- The **terminal** is the interface.

- The **shell** interprets your commands.

Once these four are clear, Linux stops being mysterious.

---

# 4. Linux Philosophy

Now we move into something deeper.

Linux isn’t just software.

It’s built on a philosophy.

And this philosophy explains why the command line is so powerful.

## Everything Is a File

This is one of the most important ideas.

In Linux, almost everything is treated as a file.

Your documents? Files.

Directories? Files.

Devices like your hard drive? Files.

Even running processes can be represented like files.

This creates a consistent model.

If everything behaves like a file, then the same tools can work everywhere.

That’s elegant design.

## Small Tools That Do One Thing Well

Linux prefers many small programs rather than one giant program.

Instead of:  “A massive app that does 50 things”

Linux says:  “Let’s build 50 small tools, each excellent at one thing.”

For example:

- `cat` shows file content.

- `find` search for files

- `grep` searches text.

- `sort` sorts.

- `wc` counts.

Each is simple.

Each is focused.

Each is reliable.

## Tools Can Be Combined

Here’s where the magic happens.

Because tools are small and focused, you can combine them.

Using pipes:

`cat file.txt | grep error | sort | uniq`

Each command passes its output to the next.

This creates workflows that are:

- Flexible

- Powerful

- Modular

You don’t need a giant application.

You build exactly what you need.

It’s like Lego for system operations.

## Text Is Powerful

Linux loves text.

Configuration files? Text.

Logs? Text.

Commands? Text.

Why?

Because text:

- Is portable

- Is searchable

- Is scriptable

- Works remotely

- Works over slow connections

Text doesn’t require graphics.

Text doesn’t require heavy interfaces.

It’s durable and efficient.

And in DevOps and cloud systems, text-based configuration is still the dominant model.

## Why This Matters

These philosophical ideas explain:

- Why the terminal matters

- Why pipes exist

- Why scripting is powerful

- Why automation is easy in Linux

You’re not just learning commands.

You’re learning a design mindset.

And once you see that mindset, Linux stops feeling random.

It starts feeling consistent.

## Transition

Now that you understand:

- The architecture (kernel, distro, shell)

- The philosophy (small tools, composability, text)

You’re ready for the fun part.

The terminal.

Because now, when you type a command, you’ll understand what’s happening behind the scenes.

But... just before jumping to command line wizardly, the very important role of the permissions in Linux (and one of the nightmares by working in a Windows Filesystem)

---

# 5. Basic Permissions

## Core Model

Every file in Linux has:

- An **owner (user)**

- A **group**

- Permissions for:

          - User (u)

          - Group (g)

          - Others (o)

Check with:

```bash
ls -l
```

Example:

```
-rwxr-xr-- 1 alice dev 4096 Jan 10 12:00 script.sh
```

Breakdown:

```
-        → file type

rwx      → user (owner)

r-x      → group

r--      → others
```

---

## File Types

| Symbol | Meaning       |
| ------ | ------------- |
| `-`    | Regular file  |
| `d`    | Directory     |
| `l`    | Symbolic link |

---

## Permission Meaning

| Permission | On File      | On Directory               |
| ---------- | ------------ | -------------------------- |
| r          | Read content | List directory contents    |
| w          | Modify       | Create/delete files inside |
| x          | Execute      | Enter directory (`cd`)     |

Important note for directories:

- Without `x`, you cannot enter the directory.

- Without `r`, you cannot list its contents.

- Without `w`, you cannot create/delete inside it.

## Numeric (Octal) Permissions

Values:

- r = 4

- w = 2

- x = 1

Examples:

| Octal | Meaning |
| ----- | ------- |
| 7     | rwx     |
| 6     | rw-     |
| 5     | r-x     |
| 4     | r--     |

Example:

```bash
chmod 755 script.sh
```

## Symbolic Mode

```bash
chmod u+x file

chmod g-w file

chmod o=r file
```

Operators:

- `+` add permission

- `-` remove permission

- `=` assign exactly

## Ownership

Change owner:

```bash
sudo chown user file

sudo chown user:group file
```

Change group only:

```bash
chgrp group file
```

---

# 6. Terminal Shortcuts

Beyond the basics of **Ctrl+C** (interrupt) and **Ctrl+L** (clear), the most useful Linux shortcuts are the ones that save you from using the arrow keys to navigate long commands.

### Navigation: Stop Using Arrow Keys

Instead of holding down the left arrow to get to the start of a long command, use these:

- **Ctrl + A**: Move cursor to the **beginning** of the line.

- **Ctrl + E**: Move cursor to the **end** of the line.

- **Alt + B**: Move back **one word** (B for Back).

- **Alt + F**: Move forward **one word** (F for Forward)

### Editing: Cut and Paste (The "Yank" Buffer)

Linux doesn't use the standard Ctrl+X/V inside the shell. It uses "Killing" and "Yanking."

- **Ctrl + U**: **Cut** everything from the cursor to the **beginning** of the line.

- **Ctrl + K**: **Cut** everything from the cursor to the **end** of the line.

- **Ctrl + W**: **Cut** the **word** before the cursor.

- **Ctrl + Y**: **Paste** (Yank) the last thing you cut.

- **Ctrl + _**: **Undo** your last edit.

### History: Never Type the Same Thing Twice

- **Ctrl + R**: **Reverse Search**. Type a few letters of a command you used yesterday, and it will find it. Press Ctrl+R again to cycle through older matches.

- **!!** (Bang-Bang): Repeats the **entire last command**

- **!$**: Represents the **last argument** of the previous command.
  
  > *Example:* You run `mkdir /long/path/name`. Next, type `cd !$` to enter it.

### Process & Control

- **Tab**: **The Holy Grail.** Autocompletes commands, file names, and paths. Double-tap for a list of all possibilities.

- **Ctrl + D**: Send "End-of-File" (EOF). It logs you out of the current shell or closes the terminal.

- **Ctrl + Z**: **Suspend** the current process. It puts the task in the background (frozen). You can bring it back with `fg` or keep it running in the background with `bg`.

- **Ctrl + S / Ctrl + Q**: **Freeze/Unfreeze** the terminal output. (Useful if a command is printing too much text and you want to read a specific line).

### Pro Tip: The "Manual" Shortcut

If you start typing a long command but realize you need to do something else first, don't delete it!
Press **Alt + #**. This puts a `#` at the start, turns the line into a "comment," and saves it to your history.

You can then press the **Up Arrow** later to bring it back and delete the `#`.

---

# 7. First Terminal Commands (Hands-on)

## Navigation

The very basic ones

```bash
pwd
ls
cd
```

- Current directory
- Listing files
- Moving between directories
- Absolute vs relative paths
- Home directory (~)

---

## File & Directory Management

```bash
mkdir
touch
rm
cp
mv
```

## File inspection

```bash
head
tail
cat
```

---

# 7. Escape Room - Level 1

Mission

A secret key is hidden somewhere in this system.

Your goal: find it.

You may use any command learned during the training.

---

## Rules

- You must work from the terminal
- Document the commands you use

---

## Hints (if needed)

1. Start by exploring your current directory.
2. Look for hidden files.
3. Search for specific keywords.
4. Check permissions if you cannot access something.

---

## Tools You Might Need

```bash
pwd
ls
ls -la
cd
cat
chmod
```

---

## Bonus Challenge

There may be a running process that should not be running.
Can you find it?
Can you stop it?

---

## Victory Condition

When you find the secret key, write it down and explain:

- Where it was
- Which commands you used
- What you learned

Good luck, Wizard.
