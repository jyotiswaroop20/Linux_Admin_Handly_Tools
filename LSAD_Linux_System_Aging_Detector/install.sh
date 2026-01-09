#!/bin/bash

echo "[+] Installing LSAD..."

# Compile the C wrapper
gcc src/lsad.c -o /usr/local/bin/lsad
chmod +x /usr/local/bin/lsad

# Create directory for Python analyzer and copy the script
mkdir -p /usr/local/lib/lsad
cp src/analyzer.py /usr/local/lib/lsad/

echo "[+] LSAD installed successfully"

