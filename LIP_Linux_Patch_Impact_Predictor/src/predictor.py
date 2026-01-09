import sys
import subprocess

package = sys.argv[1]

print("\n[LIP] Predicting patch impact...\n")

# Get package files
files = subprocess.getoutput(f"rpm -ql {package} 2>/dev/null")

if "not installed" in files:
    print("Package not installed on this system.")
    sys.exit(1)

services = set()
configs = []

for f in files.splitlines():
    if f.startswith("/etc"):
        configs.append(f)
    if "/systemd/system" in f:
        services.add(f.split("/")[-1])

# Determine risk level
risk = "LOW"
if services:
    risk = "MEDIUM"
if "kernel" in package or "openssl" in package:
    risk = "HIGH"

# Print report
print("Affected Package   :", package)
print("Affected Services  :", ", ".join(services) if services else "None")
print("Config Files       :", ", ".join(configs) if configs else "None")
print("Downtime Risk      :", risk)
print("Safe for Prod      :", "NO" if risk == "HIGH" else "YES")

