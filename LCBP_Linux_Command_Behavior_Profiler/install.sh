#!/bin/bash
set -e

echo "[+] Installing LCBP..."

# Build binary
gcc src/lcbp.c -o /usr/local/bin/lcbp
chmod +x /usr/local/bin/lcbp

# Install analyzer
mkdir -p /usr/local/lib/lcbp
cp src/analyzer.py /usr/local/lib/lcbp/analyzer.py
chmod +x /usr/local/lib/lcbp/analyzer.py

echo "[+] LCBP installed successfully"
echo "Run: lcbp <command>"

