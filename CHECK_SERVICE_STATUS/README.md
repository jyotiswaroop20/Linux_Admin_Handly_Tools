# check_service 🛠️

`check_service` ek lightweight Linux command-line utility hai jo **systemd services ka current status** check karne ke liye use hoti hai.  
Ye tool Python ke through banaya gaya hai lekin **Linux ki native command** ki tarah kaam karta hai.

---

## 📌 Purpose
System administrators aur DevOps learners ke liye:
- Service monitoring ko simple banana
- Manual `systemctl` commands ko automate karna
- Multiple services ka status ek saath dekhna

---

## ✨ Features
- Ek ya multiple services ka status check
- Simple aur readable output
- `.py` extension ki zarurat nahi
- Linux PATH me install hone ke baad direct command ki tarah run hota hai
- Automation scripts aur cron jobs ke liye suitable

---

## 🧠 Requirements
- Linux system (systemd based)
- Python 3.x installed
- `systemctl` available
- Root / sudo access (installation ke liye)

---

## ⚙️ Installation

1. Tool file ko executable banaye:
```bash
chmod +x check_service

2 - Tool ko system PATH me copy kare:
sudo cp check_service /usr/local/bin/

3 - Verify kare:
which check_service

Expected output:
/usr/local/bin/check_service

▶️ Usage
Single service check
check_service nginx
Output:
nginx : active


Multiple services check
check_service nginx sshd docker
Output:
nginx : active
sshd : active
docker : inactive

Help / Usage info
check_service --help
Output:
Usage: check_service <service_name> [service_name ...]

📤 Output Format
<service_name> : <status>
Possible status values:

active
inactive
failed
unknown

📝 Notes
Ye tool internally systemctl is-active ka use karta hai
Non-systemd Linux systems par kaam nahi karega
Output intentionally simple rakha gaya hai taaki:
Shell scripting
Cron jobs
Monitoring scripts
me easily use ho sake

🚀 Use Cases
Server health check
Startup scripts
Cron-based monitoring
Learning Linux automation with Python
Custom internal admin tools

👨💻Author
Jyotiswaroop Tripathi
Linux Administrator
