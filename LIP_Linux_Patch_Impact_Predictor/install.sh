#!/bin/bash
echo "[+] Installing LIP..."
gcc src/lip.c -o /usr/local/bin/lip
chmod +x /usr/local/bin/lip
mkdir -p /usr/local/lib/lip
cp src/predictor.py /usr/local/lib/lip/
echo "[+] Installation complete"
echo "Run: lip <package-name>"
