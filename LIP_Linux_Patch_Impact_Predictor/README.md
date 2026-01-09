# LIP – Linux Patch Impact Predictor

**Predicts the possible impact of Linux patches before applying them.**

---

## 1. Why LIP?

Before running updates like `dnf update` or `dnf update openssl`, admins often ask:  
- Which services will restart?  
- Will SSH / NGINX be affected?  
- Is production downtime likely?  

Linux has no native prediction tool. **LIP provides impact prediction BEFORE patching**, helping avoid unplanned downtime.

---

## 2. CLI Usage

Use LIP like a native Linux command:  

```bash
lip openssl
lip kernel
lip nginx
lip --help

Example Output:

[LIP] Predicting patch impact...

Affected Package   : openssl
Affected Services  : sshd
Config Files       : /etc/pki/tls/openssl.cnf
Downtime Risk      : HIGH
Safe for Prod      : NO

---

3. How It Works

User provides the package name.
LIP checks which files and services the package affects.
The Python engine predicts:
Service restarts
Configuration impact
Downtime risk

---

4. Installation

Install via script:

chmod +x install.sh
sudo ./install.sh

Post-installation:

lip <package-name>

---

5. Key Features

Detects affected services and config files
Predicts downtime risk: LOW / MEDIUM / HIGH
Advises whether it’s safe for production
Easy, lightweight, and CLI-friendly

---

6. Target Users

Linux System Administrators
DevOps Engineers / SREs
Production Support Engineers

---

Author: Jyotiswaroop Tripathi
Linux System Administrator
