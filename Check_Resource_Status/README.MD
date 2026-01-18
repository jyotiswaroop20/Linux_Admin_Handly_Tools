# system_health 🖥️

`system_health` ek command-line based Linux utility hai jo **system ke important resources ka detailed health report** generate karti hai.  
Ye tool specially **System Administrators aur DevOps learners** ke liye design kiya gaya hai.

---

## 🎯 Purpose
Daily Linux administration me jo information baar-baar check karni padti hai, usko **ek hi command me dekhna**:

- Server health overview
- Resource utilization monitoring
- Quick troubleshooting
- Automation aur cron jobs ke liye ready output

---

## ✨ Features
- System information (hostname, OS, uptime)
- CPU cores, usage aur load average
- Memory usage (total, used, free)
- Disk usage (per mount point)
- Network I/O statistics
- Logged-in users details
- Top memory-consuming processes
- Clean, readable terminal output
- Native Linux command jaisa behavior

---

## 🧠 Requirements
- Linux system (RHEL / CentOS / AlmaLinux / Ubuntu etc.)
- Python 3.x
- `psutil` Python library
- Root / sudo access (installation ke liye)

---

## ⚙️ Installation

1. Required dependency install kare:
```bash
pip install psutil

2 - Tool file ko executable banaye:
chmod +x system_health

3 - Tool ko system PATH me copy kare:
sudo cp system_health /usr/local/bin/

4 - Verify installation:
which system_health

Expected output:
/usr/local/bin/system_health

▶️ Usage
System health check run karne ke liye:
system_health

📤 Output Sections
Tool output logical sections me divided hota hai:----

System Information
CPU Status
Memory Status
Disk Usage
Network Status
Logged-in Users
Top Resource Consuming Processes

Har section clearly labelled hota hai taaki admin ko turant samajh aaye.

📝 Notes
Ye tool real-time system data read karta hai
Output intentionally human-readable rakha gaya hai
Monitoring scripts aur cron jobs ke saath use kiya ja sakta hai
Lightweight hai, system pe heavy load nahi dalta


🚀 Common Use Cases
Daily server health check
Pre / post maintenance verification
Troubleshooting performance issues
Automation practice projects
DevOps / SysAdmin interviews ke liye demo tool

👨‍💻 Author
Jyotiswaroop Tripathi
Linux System Administrator