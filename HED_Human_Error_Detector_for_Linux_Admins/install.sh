#!/bin/bash

echo "[+] Installing HED..."

# Compile the C wrapper
gcc src/hed.c -o /usr/local/bin/hed
chmod +x /usr/local/bin/hed

# Create directory for Python detector and copy the script
mkdir -p /usr/local/lib/hed
cp src/detector.py /usr/local/lib/hed/

echo "[+] HED installed successfully"
echo "Run: hed <command>"

