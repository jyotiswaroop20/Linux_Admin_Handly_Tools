#!/bin/bash

echo "[+] Installing LCMT..."

gcc src/lcmt.c -o /usr/local/bin/lcmt
chmod +x /usr/local/bin/lcmt

mkdir -p /usr/local/lib/lcmt
cp src/tracker.py /usr/local/lib/lcmt/

mkdir -p /var/lib/lcmt

echo "[+] LCMT installed successfully"
echo "Run: lcmt snapshot"

