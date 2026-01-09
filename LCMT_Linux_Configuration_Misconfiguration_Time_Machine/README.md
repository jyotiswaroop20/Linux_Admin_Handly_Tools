# LCMT – Linux Configuration Misconfiguration Time Machine

LCMT is a lightweight Linux CLI tool that tracks configuration changes in `/etc` and helps system administrators quickly identify **what changed, when it changed, and which configuration files caused system issues**.

It works like a **time machine for Linux configuration files**, without requiring Git or repositories.

---

## Problem Statement

Linux administrators often face this situation:

> *“Yesterday everything was working. Today the service is broken.”*

By default, Linux:

* Does not maintain configuration history
* Does not clearly show which config file changed
* Does not tell when a breaking change was introduced

**LCMT solves this problem safely and simply, without using Git.**

---

## What LCMT Does

* Takes snapshots of `/etc`
* Stores cryptographic hashes of configuration files
* Compares snapshots over time
* Detects configuration drift
* Shows modified, new, and deleted config files
* Helps identify root cause of breakages

---

## CLI Usage (Native Linux Command Style)

```bash
lcmt snapshot
lcmt diff
lcmt history
```

### Example

```bash
lcmt snapshot
lcmt diff
```

**Sample Output**

```
Modified or New:
/etc/ssh/sshd_config
```

---

## How LCMT Works (Architecture)

### 1. `lcmt snapshot`

* Scans `/etc`
* Calculates SHA256 hash of each config file
* Stores snapshot with timestamp

### 2. `lcmt diff`

* Compares the last two snapshots
* Detects:

  * Modified files
  * New configuration files
  * Deleted configuration files

### 3. `lcmt history`

* Lists all available snapshots
* Helps navigate configuration timeline

---

## Installation

```bash
chmod +x install.sh
sudo ./install.sh
```

After installation:

```bash
lcmt snapshot
```

---

## Sample Workflow (Real Testing)

### ⚠ Important Before Testing

* Root privileges required (reads `/etc`)
* Do **NOT** test directly on production
* Best practice: Use VM or test server

---

### Step 1: First Snapshot (Baseline)

```bash
sudo lcmt snapshot
```

**What happens internally:**

* All files under `/etc` are scanned
* SHA256 hash is generated for each file
* Snapshot file created:

```
/var/lib/lcmt/1704889001.snap
```

**Output**

```
Snapshot created: 1704889001
```

This is your **baseline**.

---

### Step 2: Make a Safe Configuration Change

#### Example 1: SSH (Safe Change)

```bash
sudo cp /etc/ssh/sshd_config /tmp/sshd_config.bak
sudo echo "# LCMT test" >> /etc/ssh/sshd_config
```

* File content changes
* Hash changes
* No service restart required

#### Example 2: Nginx (If Installed)

```bash
sudo echo "# test" >> /etc/nginx/nginx.conf
```

---

### Step 3: Second Snapshot

```bash
sudo lcmt snapshot
```

Output:

```
Snapshot created: 1704889305
```

---

### Step 4: Compare Snapshots

```bash
sudo lcmt diff
```

**Expected Output**

```
Configuration changes detected:
Modified or New: /etc/ssh/sshd_config
Modified or New: /etc/nginx/nginx.conf
```

---

### Step 5: View Snapshot History

```bash
sudo lcmt history
```

Output:

```
Available snapshots:
1704889001.snap
1704889305.snap
```

---

## What LCMT Detects

| Change Type         | Detected           |
| ------------------- | ------------------ |
| File content change | Yes                |
| New config file     | Yes                |
| Deleted config file | Yes                |
| Permission change   | Future enhancement |
| Ownership change    | Future enhancement |

---

## LCMT vs Git for Configuration Tracking

| Feature               | Git       | LCMT |
| --------------------- | --------- | ---- |
| Needs repository init | Yes       | No   |
| Safe for production   | Risky     | Yes  |
| Tracks full `/etc`    | Difficult | Easy |
| Lightweight           | No        | Yes  |

---

## Use Cases

* Linux system administrators
* Production incident debugging
* Configuration drift detection
* Post-change root cause analysis
* Interview/demo projects

---

## Author

**Jyotiswaroop Tripathi**
Linux System Administrator

---

*LCMT is designed to be simple, safe, and production-friendly.*

