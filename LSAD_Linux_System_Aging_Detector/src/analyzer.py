import os
import subprocess

# Get system uptime in seconds and convert to days
uptime = subprocess.getoutput("cut -d. -f1 /proc/uptime")
uptime_days = int(float(uptime) // 86400)

# Count zombie processes
zombies = subprocess.getoutput(
    "ps aux | awk '{print $8}' | grep -c Z"
)

# Get disk usage percentage for root filesystem
disk = subprocess.getoutput(
    "df / | tail -1 | awk '{print $5}' | tr -d '%'"
)

# Calculate system age score
score = 100
score -= uptime_days
score -= int(zombies) * 5
score -= int(disk) // 2

# Determine system status
status = "HEALTHY"
if score < 70:
    status = "AGING"
if score < 50:
    status = "OLD"

# Display LSAD report
print("\n------ LSAD REPORT ------")
print(f"System Age Score : {max(score,0)} / 100 ({status})")
print(f"Uptime (days) : {uptime_days}")
print(f"Zombie Processes: {zombies}")
print(f"Disk Usage (%) : {disk}")

if status != "HEALTHY":
    print("Recommendation : Reboot and system cleanup suggested")

