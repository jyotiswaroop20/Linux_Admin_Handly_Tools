import os
import sys
import hashlib
import time

BASE_DIR = "/var/lib/lcmt"
ETC_DIR = "/etc"

os.makedirs(BASE_DIR, exist_ok=True)


def file_hash(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return None


def snapshot():
    ts = str(int(time.time()))
    snap_file = f"{BASE_DIR}/{ts}.snap"

    with open(snap_file, "w") as out:
        for root, _, files in os.walk(ETC_DIR):
            for f in files:
                path = os.path.join(root, f)
                h = file_hash(path)
                if h:
                    out.write(f"{path}|{h}\n")

    print(f"Snapshot created: {ts}")


def diff():
    snaps = sorted(os.listdir(BASE_DIR))

    if len(snaps) < 2:
        print("Not enough snapshots to compare.")
        return

    old = open(f"{BASE_DIR}/{snaps[-2]}").readlines()
    new = open(f"{BASE_DIR}/{snaps[-1]}").readlines()

    old_set = set(old)
    new_set = set(new)

    print("\nConfiguration changes detected:\n")

    for line in new_set - old_set:
        print("Modified or New:", line.split("|")[0])

    for line in old_set - new_set:
        print("Removed:", line.split("|")[0])


def history():
    print("\nAvailable snapshots:\n")

    for s in sorted(os.listdir(BASE_DIR)):
        print(s)


if sys.argv[1] == "snapshot":
    snapshot()
elif sys.argv[1] == "diff":
    diff()
elif sys.argv[1] == "history":
    history()
else:
    print("Invalid option")

