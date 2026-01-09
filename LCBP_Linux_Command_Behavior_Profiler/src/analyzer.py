#!/usr/bin/env python3

log_file = "/tmp/lcbp_trace.log"

file_ops = 0
network_ops = 0

FILE_SYSCALLS = (
    "openat(", "unlinkat(", "renameat(", "mkdirat(",
    "rmdir(", "creat(", "write("
)

NET_SYSCALLS = ("connect(", "sendto(", "recvfrom(")

try:
    with open(log_file, "r", errors="ignore") as f:
        for line in f:
            if any(call in line for call in FILE_SYSCALLS):
                file_ops += 1
            if any(call in line for call in NET_SYSCALLS):
                network_ops += 1
except FileNotFoundError:
    print("[LCBP] Trace log not found")
    exit(1)

risk = "LOW"

if network_ops > 0 and file_ops > 50:
    risk = "HIGH"
elif network_ops > 0:
    risk = "MEDIUM"
elif file_ops > 500:
    risk = "HIGH"
elif file_ops > 100:
    risk = "MEDIUM"

print("\n------ LCBP REPORT ------")
print(f"File Operations : {file_ops}")
print(f"Network Connections : {network_ops}")
print(f"Risk Score : {risk}")

