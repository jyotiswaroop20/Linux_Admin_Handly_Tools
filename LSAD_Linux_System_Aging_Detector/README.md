# LSAD – Linux System Aging Detector

**Detects how “old” or “degraded” a Linux system has become over time and provides maintenance recommendations.**

---

## 1. Problem This Solves

Admins often say:  
*"The system feels slow, but nothing is technically wrong."*

Linux has no native concept of **system aging**.  
**LSAD introduces:**
- System Age Score
- Health degradation indicators
- Preventive maintenance insights

---

## 2. CLI Usage

LSAD works like a native Linux command:  

```bash
lsad
lsad --help

---

## Sample Output:
System Age Score : 78 / 100 (OLD)
Uptime           : 143 days
Zombie Processes : 7
Disk Usage       : 82%
Recommendation   : Reboot cycle overdue

---

## 3. How It Works
LSAD evaluates the system based on:
System uptime
Zombie processes
Disk usage
Long-running processes
Load average
All factors contribute to a System Age Score, which indicates the system’s health status.

---

## 4. Installation
Installation script: install.sh
Steps:

chmod +x install.sh
sudo ./install.sh


What it does:
Compiles the C CLI wrapper (lsad) and places it in /usr/local/bin/
Copies the Python analyzer to /usr/local/lib/lsad/
Makes lsad executable

## Post-installation:

lsad

Run the tool to get your system health and aging report.

---


## 5. Key Features

Calculates a System Age Score out of 100
Detects zombie processes and high disk usage
Highlights aging systems with HEALTHY / AGING / OLD status
Provides maintenance recommendations such as reboot or cleanup
Lightweight, safe, and easy to run from the CLI

---

## 6. Target Users

LSAD is useful for:
Linux System Administrators
DevOps Engineers / SREs
Production Support Engineers
Linux learners and enthusiasts

---

## 7. Notes

LSAD does not modify system files
Only monitors and reports system aging metrics
Should be run periodically for preventive maintenance

---

## Author: Jyotiswaroop Tripathi
## Linux System Administrator
