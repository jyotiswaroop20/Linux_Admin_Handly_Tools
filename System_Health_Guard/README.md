# System Health Guard (sysguard)

**System Health Guard (sysguard)** is an intelligent Linux system monitoring and file search tool designed for system administrators and DevOps engineers. It performs deep system health analysis, reports only real problems with clear solutions, and provides fast file & directory search using both `find` and `locate` — all through a single native-style command.

This tool avoids noisy or false reports. If your system is healthy, it gives a clean status. If issues exist, it explains them in simple language with severity and recommended actions.

---

## 🚀 Key Features

### 🖥️ Intelligent System Health Scan

* Disk usage check (>= 90%)
* Inode usage check
* Failed systemd services detection
* High CPU usage detection
* High memory usage detection
* Swap usage monitoring (> 80%)
* RAID degraded status check
* Filesystem errors (EXT4 / XFS)
* Load average vs CPU core comparison
* Docker container failure detection
* Kubernetes node health check

### ⚠️ Severity Levels

Each issue is reported with a clear severity:

* **LOW** – informational
* **MEDIUM** – needs attention
* **CRITICAL** – immediate action required

### 🧠 Smart Reporting

* Reports **only real problems**
* No unnecessary or false alerts
* If no issues are found → **CLEAN system status**
* Every issue includes a **simple solution**

### 🔍 File & Directory Search

* Searches **files and directories**
* Uses **locate** (fast database-based search)
* Uses **find** (deep and accurate search)
* Works with full name or partial keyword
* Displays full paths

### 🔐 Security & Compatibility

* Must be run as **root or with sudo**
* Uses only native Linux commands
* No external dependencies
* Works on most modern Linux distributions

---

## 📦 Installation (System-wide Command)

Follow these steps to install `sysguard` as a native Linux command.

### Step 1: Make the script executable

```bash
chmod +x sysguard
```

### Step 2: Copy to system PATH

```bash
sudo cp sysguard /usr/local/bin/
```

### Step 3: Verify installation

```bash
which sysguard
```

Expected output:

```
/usr/local/bin/sysguard
```

Now you can run `sysguard` from anywhere.

---

## 🧪 Usage

### 1️⃣ System Health Scan

Scans the entire system and reports only real issues.

```bash
sysguard --scan-logs
```

#### Example Output (Issues Found)

```
❌ [CRITICAL] Disk Usage High
📄 Details:
/dev/sda1 95%
🛠️ Solution: Free disk space or extend filesystem
```

#### Example Output (Clean System)

```
✅ System Health Status: CLEAN
No issues detected. No action required.
```

---

### 2️⃣ File & Directory Search

Search for any file or directory using full or partial name.

```bash
sysguard --find nginx
```

This command:

* Searches using `locate`
* Searches using `find`
* Displays up to 20 matching paths

---

## 🧩 Why sysguard?

Normally, an administrator must manually:

* Check disk and inode usage
* Inspect failed services
* Analyze CPU, memory, and swap
* Look for RAID or filesystem errors
* Investigate Docker / Kubernetes health
* Search files across the filesystem

**sysguard does all of this with one command.**

---

## 🛠️ Designed For

* Linux System Administrators
* DevOps Engineers
* Production & Enterprise servers
* Troubleshooting & audits
* Daily health monitoring

---

## 👤 Author

**Jyotiswaroop Tripathi**
Linux System Administrator

---

## ✅ Summary

* Clean output
* Real problem detection
* Easy-to-understand solutions
* Fast search + deep scan
* Production-ready & safe

**System Health Guard (sysguard)** is built to keep your Linux systems stable, clean, and under control.

