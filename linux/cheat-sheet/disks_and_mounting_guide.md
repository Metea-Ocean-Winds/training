# Disks, Partitions & Mounting Guide

---

# The Chain

```
Disk  →  Partition table  →  Partition  →  Filesystem  →  Mount point
/dev/sda    GPT / MBR          /dev/sda1      ext4            /
```

---

# Device Names

| Name             | Meaning                         |
| ---------------- | ------------------------------- |
| `/dev/sda`       | First SATA/SCSI/USB disk        |
| `/dev/sda1`      | Partition 1 of `sda`            |
| `/dev/nvme0n1`   | First NVMe disk                 |
| `/dev/nvme0n1p1` | Partition 1 of that NVMe        |
| `/dev/vda`       | Virtual disk (cloud VMs)        |
| `/dev/loop0`     | File used as a disk             |

---

# Partition Tables

|                | MBR (`dos`) | GPT       |
| -------------- | ----------- | --------- |
| Max disk       | 2 TB        | Huge      |
| Max partitions | 4 primary   | 128       |
| Boot           | BIOS        | UEFI      |

---

# Filesystems

| Type    | Use                                 |
| ------- | ----------------------------------- |
| `ext4`  | Linux default                       |
| `xfs`   | Large files / servers               |
| `vfat`  | USB, EFI partition                  |
| `ntfs`  | Windows                             |
| `swap`  | Swap space                          |
| `tmpfs` | In RAM, lost on reboot              |

---

# Inspect (read-only)

```bash
lsblk                     # disks & partitions tree
lsblk -f                  # + fs type, UUID, mount point
sudo blkid                # UUIDs
sudo fdisk -l             # partition tables (ONLY with -l)
df -h                     # free space
df -hT                    # + fs type
du -sh folder             # folder size
sudo du -sh /var/* | sort -h
free -h                   # RAM & swap
swapon --show             # swap devices
findmnt                   # mount tree
findmnt /                 # what is on /
```

---

# Mount / Unmount

```bash
sudo mkdir -p /mnt/data
sudo mount /dev/sdb1 /mnt/data
sudo mount -o ro /dev/sdb1 /mnt/data            # read-only
sudo mount -t tmpfs -o size=50M tmpfs /mnt/demo # RAM disk
sudo umount /mnt/data
```

***Target is busy***

```bash
sudo lsof +D /mnt/data
sudo fuser -vm /mnt/data
```

---

# /etc/fstab

```
# <device>      <mount point>  <type>  <options>         <dump> <pass>
UUID=xxxx-xxxx  /data          ext4    defaults,nofail   0      2
```

| Option      | Meaning                          |
| ----------- | -------------------------------- |
| `defaults`  | Standard options                 |
| `ro` / `rw` | Read-only / read-write           |
| `noexec`    | Programs cannot run from it      |
| `nofail`    | Boot even if the device is missing |
| `pass`      | fsck order: `1` root, `2` others, `0` skip |

Always test after editing:

```bash
sudo findmnt --verify
sudo mount -a
```

---

# New Disk Workflow

⚠️ Steps 2–3 erase data. Double-check the device!

```bash
lsblk                                 # 1. identify  (/dev/sdb)
sudo parted /dev/sdb mklabel gpt      # 2. partition table
sudo parted -a optimal /dev/sdb mkpart primary ext4 0% 100%
sudo mkfs.ext4 /dev/sdb1              # 3. filesystem
sudo mkdir /data                      # 4. mount point
sudo mount /dev/sdb1 /data            # 5. mount
sudo blkid /dev/sdb1                  # 6. UUID
sudoedit /etc/fstab                   # 7. add UUID line with nofail
sudo findmnt --verify && sudo mount -a  # 8. verify
```
