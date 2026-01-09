# LCBP – Linux Command Behavior Profiler

LCBP (Linux Command Behavior Profiler) is a Linux administration and security tool that analyzes the actual runtime behavior of Linux commands before trusting them in production environments.  
Instead of guessing what a command might do, LCBP observes real system calls and generates a risk-based report to help prevent accidental damage caused by human error.

---

## 🚀 Project Overview

Linux administrators often execute powerful commands directly on live systems.  
A single wrong command can result in data loss, service outages, or security incidents.  

**LCBP solves this problem by:**
- Tracing real system calls using `strace`
- Analyzing file and network activity
- Generating a simple and understandable risk score

---

## ⭐ Why LCBP Is Unique

Most existing Linux tools:
- Monitor system health
- Detect vulnerabilities
- Log events after damage has already occurred

**LCBP is different:**
- Profiles command behavior, not system state
- Helps administrators understand command impact before execution
- Focuses on human error prevention

---

## 👥 Who Can Use This Tool

LCBP is useful for:
- Linux System Administrators
- Site Reliability Engineers (SREs)
- Production Support Engineers
- Linux learners and trainees

---

## 🛠 How It Works (MVP Flow)

1. User runs a Linux command through `lcbp`
2. `lcbp.c` executes the command using `strace`
3. All system calls are logged
4. `analyzer.py` parses the trace log and:
   - Counts file operations
   - Detects network activity
   - Generates a risk score
5. A final behavior report is displayed

---

## 📂 Project Structure

LCBP_Linux_Command_Behavior_Profiler/
├── src/
│ ├── lcbp.c # C wrapper to execute commands with strace
│ ├── analyzer.py # Python script to analyze trace logs
├── install.sh # Installation script
└── README.md # Project documentation


---

## ▶️ Usage (Like a Normal Linux Command)

```bash
lcbp ls /
lcbp dnf update
lcbp rm -rf /tmp/test
lcbp --help


[LCBP] Profiling command...
[LCBP] Command execution completed.
[LCBP] Generating report...

------ LCBP REPORT ------
File Operations       : 342
Network Connections   : 1
Risk Score            : HIGH


🔍 Report Explanation

File Operations
Number of file-related system calls (open, read, write, delete)
Network Connections
Number of detected network or socket connection attempts
Risk Score
LOW → Safe command
MEDIUM → Review before production use
HIGH → Dangerous, approval recommended

🎯 Use Cases
Validate risky commands before production execution
Analyze third-party scripts
Train junior administrators safely
Prevent accidental rm -rf disasters

👤 Author
Jyotiswaroop Tripathi
Linux System Administrator
