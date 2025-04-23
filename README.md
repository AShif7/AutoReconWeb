# AutoReconWeb
"A fast automated web scanner with animation and recon modules"
# AutoReconWeb

**AutoReconWeb** is an advanced, fast, and animated web reconnaissance tool for cybersecurity professionals. Just enter a target IP or domain, and this tool performs step-by-step scanning with movie-style animation and detailed results.

## Features

- Cool hacking-style animated interface
- Nmap scan with default scripts and version detection
- Web technology detection (server, powered-by headers)
- Directory brute-force using Gobuster
- robots.txt file check
- Admin path detection (common paths)
- Basic SQL injection (SQLi) error-based check

## Demo

![Banner](https://img.shields.io/badge/Style-Terminal-green)
# Installation Guide (for Kali Linux)

Follow the steps below to install and run AutoReconWeb:

### 1. Clone the Repository

```bash
git clone https://github.com/AShif7/AutoReconWeb.git
cd AutoReconWeb


---

2. Install Python Requirements

Make sure Python 3 is installed.

pip3 install -r requirements.txt


---

3. Install Required Tools (nmap and gobuster)

These tools are needed for scanning. Run:

sudo apt update
sudo apt install nmap gobuster -y


---

4. Run the Tool

Use the command below to start scanning:

python3 autorecon.py --target example.com

> Replace example.com with your target domain or IP address.




---

Example

python3 autorecon.py --target 192.168.0.101

The tool will show terminal animation and scan the target step by step.


---

Notes

This tool is for educational purposes only.

Do not scan any system without proper authorization.


---
___        _              _____                         
   /   |  ____(_)___ ___     / ___/______________ _____ ___ 
  / /| | / __/ / __ `__ \    \__ \/ ___/ ___/ __ `/ __ `__ \
 / ___ |/ /_/ / / / / / /   ___/ / /__/ /  / /_/ / / / / / /
/_/  |_/___/_/_/ /_/ /_/   /____/\___/_/   \__,_/_/ /_/ /_/
