# HED – Human Error Detector for Linux Admins

**Detects dangerous or destructive Linux commands BEFORE execution and warns the administrator.**

---

## 1. Problem This Solves

Most Linux outages are caused by **human mistakes**, not software bugs:  

- `rm -rf /`  
- `rm -rf /var/log/*`  
- `chmod 777 /`  
- `iptables -F`  
- `chown root:root /`  

Linux executes these commands without warnings. There is **no native safety layer**.  
**HED adds an intelligent safety net** to prevent accidental disasters.

---

## 2. CLI Usage

HED works like a native Linux tool. Example usage:

```
hed rm -rf /var/log
hed chmod 777 /
hed iptables -F
hed --help

---

Sample Output:
WARNING: Potentially dangerous command detected!
Command : rm -rf /var/log
Reason  : Recursive delete on system directory
Suggested alternative:
rm -rf /var/log/myapp/*
Continue? (yes/no):

---

3. How It Works (Architecture)
User runs a command via hed
C wrapper forwards the command to the Python detector
Python analyzes the command for:
Known dangerous patterns
System-critical paths
If safe → executes the command
If dangerous → prompts user for confirmation

---

4. Installation
Installation script: install.sh
Steps:
chmod +x install.sh
sudo ./install.sh

What it does:
Compiles the C wrapper (hed) and places it in /usr/local/bin/
Copies the Python detector (detector.py) to /usr/local/lib/hed/
Makes hed executable
Post-installation:
hed <command>
Run any command safely, with HED protecting against accidental destructive operations.

---

5. Key Features
Detects dangerous Linux commands before execution
Prevents accidental deletion of critical system files
Suggests safer alternatives when possible
Easy-to-use command-line interface
Lightweight and system-friendly

---

6. Target Users
HED is useful for:
Linux System Administrators
DevOps Engineers / SREs
Production Support Engineers
Linux learners and trainees

---

7. Notes
HED does not modify system commands; it wraps and checks them
Only detects commands included in its predefined patterns
Users should still exercise caution when running destructive commands

---

Author: Jyotiswaroop Tripathi
Linux System Administrator
