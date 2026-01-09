import sys
import subprocess

command = " ".join(sys.argv[1:])

danger_patterns = [
    ("rm -rf /", "Recursive delete on root filesystem"),
    ("rm -rf /var", "Recursive delete on system logs"),
    ("chmod 777 /", "Dangerous permission on root directory"),
    ("iptables -F", "Firewall rules flush"),
    ("chown root:root /", "Ownership change on root")
]

for pattern, reason in danger_patterns:
    if pattern in command:
        print("\nWARNING: Potentially dangerous command detected!")
        print("Command :", command)
        print("Reason  :", reason)

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != "yes":
            print("Execution aborted.")
            sys.exit(1)
        break

print("\n[HED] Executing command...\n")
subprocess.call(command, shell=True)
