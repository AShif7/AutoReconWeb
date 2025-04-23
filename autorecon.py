
# AutoReconWeb - Fast & Advanced Automated Website Scanner with Movie-Style Animation

import argparse
import subprocess
import requests
import concurrent.futures
import time
import itertools
import sys
from colorama import init, Fore, Style
import pyfiglet

init(autoreset=True)

def animated_banner():
    banner = pyfiglet.figlet_format("AutoReconWeb")
    for line in banner.split("\n"):
        print(Fore.CYAN + line)
        time.sleep(0.02)

def spinner(msg, duration=2):
    spinner_cycle = itertools.cycle(["|", "/", "-", "\\"])
    end_time = time.time() + duration
    print(Fore.YELLOW + msg, end=" ")
    while time.time() < end_time:
        sys.stdout.write(next(spinner_cycle))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")
    print("Done!")

def fake_hacking_intro(target):
    steps = [
        f"[+] Target Acquired: {target}",
        "[+] Establishing secure connection...",
        "[+] Bypassing firewalls...",
        "[+] Injecting scanning modules...",
        "[+] Recon Engine Initialized"
    ]
    for step in steps:
        print(Fore.GREEN + step)
        time.sleep(1)

    progress = [
        ("[=         ] 10% - Scanning Ports", 0.5),
        ("[====      ] 40% - Gathering Technologies", 0.6),
        ("[=======   ] 70% - Crawling Directories", 0.5),
        ("[==========] 100% - Recon Ready!", 0.7)
    ]
    for line, delay in progress:
        print(Fore.YELLOW + line)
        time.sleep(delay)

def nmap_scan(target):
    spinner("[+] Running Nmap scan")
    subprocess.run(["nmap", "-sC", "-sV", target])

def tech_detect(target):
    print(Fore.YELLOW + "[+] Detecting Web Technologies...")
    try:
        response = requests.get(f"http://{target}", timeout=5)
        print(Fore.GREEN + "[+] Server:", response.headers.get("Server"))
        print(Fore.GREEN + "[+] X-Powered-By:", response.headers.get("X-Powered-By"))
    except Exception as e:
        print(Fore.RED + "[-] Failed to connect:", e)

def dirb_scan(target):
    spinner("[+] Running Directory Brute Force (gobuster)")
    try:
        subprocess.run(["gobuster", "dir", "-u", f"http://{target}", "-w", "/usr/share/wordlists/dirb/common.txt"])
    except Exception as e:
        print(Fore.RED + "[-] Gobuster failed:", e)

def check_robots_txt(target):
    print(Fore.YELLOW + "[+] Checking robots.txt...")
    try:
        response = requests.get(f"http://{target}/robots.txt", timeout=5)
        if response.status_code == 200:
            print(Fore.GREEN + "[+] robots.txt found:")
            print(response.text)
        else:
            print(Fore.RED + "[-] robots.txt not found")
    except Exception as e:
        print(Fore.RED + "[-] Error checking robots.txt:", e)

def check_path(target, path):
    try:
        response = requests.get(f"http://{target}{path}", timeout=5)
        color = Fore.GREEN if response.status_code == 200 else Fore.YELLOW
        print(color + f"[*] {path} -> Status Code: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"[-] Error accessing {path}:", e)

def check_common_paths(target):
    print(Fore.YELLOW + "[+] Checking common admin paths...")
    paths = ["/admin", "/login", "/config", "/dashboard", "/backup"]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_path, target, path) for path in paths]
        concurrent.futures.wait(futures)

def check_basic_sqli(target):
    print(Fore.YELLOW + "[+] Checking for basic SQLi errors...")
    test_url = f"http://{target}/?id=1'"
    try:
        response = requests.get(test_url, timeout=5)
        errors = ["mysql", "syntax error", "Warning", "ODBC"]
        for error in errors:
            if error.lower() in response.text.lower():
                print(Fore.RED + f"[!] Possible SQLi found at {test_url}")
                return
        print(Fore.GREEN + "[-] No SQLi signs detected")
    except Exception as e:
        print(Fore.RED + "[-] Error testing SQLi:", e)

def main():
    parser = argparse.ArgumentParser(description="AutoReconWeb - Fast Automated Website Scanner")
    parser.add_argument("--target", help="Target IP or domain", required=True)
    args = parser.parse_args()
    target = args.target

    animated_banner()
    fake_hacking_intro(target)

    nmap_scan(target)
    tech_detect(target)
    dirb_scan(target)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(check_robots_txt, target)
        executor.submit(check_common_paths, target)
        executor.submit(check_basic_sqli, target)

if __name__ == "__main__":
    main()
