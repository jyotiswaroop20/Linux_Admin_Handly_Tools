# bulk_useradd 👥

`bulk_useradd` is a command-line Linux utility designed to **create multiple users interactively in a single run**.  
The tool is built for **System Administrators** who want a secure, repeatable, and efficient way to manage user accounts.

---

## 🎯 Purpose
Creating users manually using `useradd` repeatedly can be time-consuming and error-prone.  
This tool simplifies the process by:
- Taking all required inputs interactively
- Allowing continuous user creation until exit
- Handling password hashing securely
- Working like a native Linux command

---

## ✨ Features
- Interactive user creation loop (add unlimited users in one run)
- Accepts:
  - Username
  - Display name (GECOS)
  - Login shell
  - Home directory
  - Password (hidden input)
- Passwords are stored using **SHA-512 hashing**
- Directly updates `/etc/shadow` securely
- Works with **root** and **sudo** users
- Clean terminal-based interface
- Native Linux command-style behavior (no `.py` required)

---

## 🧠 Requirements
- Linux system (systemd-based preferred)
- Python 3.x
- Root privileges or sudo access
- Standard Linux user management utilities (`useradd`)

---

## ⚙️ Installation

1. Make the tool executable:
```bash
chmod +x bulk_useradd

2 - Copy it to a directory in system PATH:
sudo cp bulk_useradd /usr/local/bin/

3 - Verify installation:
which bulk_useradd

Expected output:
/usr/local/bin/bulk_useradd

▶️ Usage
Run the tool with root or sudo:
sudo bulk_useradd

The tool will continuously prompt for user details until you type:
exit

🔐 Security Considerations
Password input is fully hidden (no echo on terminal)
Passwords are never stored in plain text
SHA-512 hashing is used before saving credentials
No sensitive data is logged or written to files
Requires elevated privileges to ensure system safety

📌 Input Details
For each user, the tool collects:
Username - 
Full name (display name) - 
Login shell (default supported) - 
Home directory (default supported) - 
Password (with confirmation) - 
Defaults are automatically applied if optional values are skipped.

🧪 Common Use Cases
Bulk user onboarding on Linux servers
Lab / training environment setup
Automation practice for SysAdmins
Secure user provisioning
Interview and portfolio demonstration tool

📝 Notes
Users are created using standard Linux mechanisms
Home directories are created automatically
Suitable for interactive administration, not unattended execution
Designed for clarity, safety, and learning purposes

🔮 Future Enhancements are going on-----
Group assignment during user creation
Password complexity enforcement
Account expiry and aging options
CSV-based bulk user import
Logging and audit support
RPM / DEB package distribution

👨💻Author
Jyotiswaroop Tripathi
Linux System Administrator
