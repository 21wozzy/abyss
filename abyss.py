import os
import time
import subprocess
import sys
import requests

# Function to clear the screen
def clear_screen():
    os.system('clear')

# Function to show the initial banner
def show_banner():
    clear_screen()
    print("""
    ⚠️ Creator's message: This tool should be used with caution. I will not be responsible for any illegal actions. 
    Created by: crowley
    
    ███████╗████████╗██╗░░░░░██╗░░░░░░░██████╗░░██████╗░██╗░░░░░░██████╗░
    ╚══███╔╝╚══██╔══╝██║░░░░░██║░░░░░░██╔══██╗██╔════╝░██║░░░░░██╔══██╗
    ░░░██╔╝░░░░██║░░░██║░░░░░██║░░░░░░██║░░██║╚█████╗░░██║░░░░░██████╔╝
    ░░░████║░░░░██║░░░██║░░░░░██║░░░░░░██║░░██║░╚═══██╗░██║░░░░░██╔══██╗
    ░░░╚══╝░░░░░██║░░░███████╗███████╗░██████╔╝██████╔╝███████╗░██║░░██║
    ░░░░░░░░░░░░╚═╝░░░╚══════╝╚══════╝░╚═════╝░╚═════╝░╚══════╝░╚═╝░░╚═╝
    
    21wozzy - Social Media Links:
    - TikTok: @croowleyy
    - Instagram: @croowleey
    """)

    time.sleep(2)

# Function for scanning ports with Nmap
def nmap_scan(ip):
    print(f"Scanning ports of {ip} with Nmap...")
    subprocess.run(f"nmap {ip}", shell=True)
    input("\nPress Enter to return to the menu...")

# Function for checking website status
def check_website_status():
    url = input("Enter the website URL (e.g., https://example.com): ")
    response = subprocess.run(f"curl -Is {url} | head -n 1", shell=True, capture_output=True, text=True)
    print(f"Status: {response.stdout}")
    input("\nPress Enter to return to the menu...")

# Function for checking DDoS protection
def check_ddos_protection(target_url):
    print(f"Checking DDoS protection for {target_url}...")
    subprocess.run(f"curl -I {target_url}", shell=True)
    input("\nPress Enter to return to the menu...")

# Function for downloading all packages in Termux (apt, pip)
def download_all_packages():
    print("⚠️ WARNING: You are about to download all available packages in Termux.")
    print("This may take a long time and consume a lot of space!")
    print("⏳ Countdown: 10 seconds... Get out now if you have limited space!")
    
    for i in range(10, 0, -1):
        print(f"{i} seconds remaining")
        time.sleep(1)

    subprocess.run("pkg update -y && pkg upgrade -y", shell=True)
    subprocess.run("pkg install $(pkg list -a) -y", shell=True)
    subprocess.run("pip install --upgrade pip", shell=True)
    subprocess.run("pip freeze | cut -d = -f 1 | xargs pip install --upgrade", shell=True)
    
    print("\nAll packages installed!")
    input("\nPress Enter to return to the menu...")

# Function for secret tools access (password required)
def secret_tools():
    clear_screen()
    print("""
    🔐 Welcome to Secret Tools! 🔐
    
    Instructions for using each option:
    
    1. **Amass**: Tool for subdomain enumeration. Use it to find subdomains of a domain.
    2. **Sublist3r**: Another subdomain enumeration tool. It can be useful to cross-check results from Amass.
    3. **Nmap**: Network mapper. Used to scan for open ports and services running on a server.
    4. **Nikto**: Web server scanner. Scans web servers for security vulnerabilities.
    5. **Whois**: Domain information tool. It shows who owns a domain and other registration details.
    
    To use these tools, simply enter the number corresponding to the tool you want to use. 
    Note: Some tools may require additional setup. Ensure they are installed in Termux before use.
    """)

    password = input("Enter the password to access secret tools: ")
    if password == "free":
        print("🔑 Access granted to secret OSINT tools!")
        print("🔍 Scanning tools...")
        osint_tools()
    else:
        print("❌ Incorrect password!")
        input("\nPress Enter to return to the menu...")

# OSINT Tools Function (inside secret tools)
def osint_tools():
    print("""
    🛠️ OSINT Tools (compatible with Termux):
    1. Amass - Subdomain enumeration
    2. Sublist3r - Subdomain enumeration
    3. Nmap - Network scanning
    4. Nikto - Web server scanner
    5. Whois - Domain information
    """)

    tool_choice = input("Choose a tool number: ")

    if tool_choice == "1":
        subprocess.run("amass enum -d example.com", shell=True)
    elif tool_choice == "2":
        subprocess.run("sublist3r -d example.com", shell=True)
    elif tool_choice == "3":
        ip = input("Enter the IP to scan: ")
        subprocess.run(f"nmap {ip}", shell=True)
    elif tool_choice == "4":
        url = input("Enter the URL to scan: ")
        subprocess.run(f"nikto -h {url}", shell=True)
    elif tool_choice == "5":
        domain = input("Enter the domain to query: ")
        subprocess.run(f"whois {domain}", shell=True)
    else:
        print("❌ Invalid option")
    input("\nPress Enter to return to the menu...")

# Main menu
def main():
    show_banner()

    while True:
        clear_screen()
        print("""
        Select an option:
        1. Scan ports with Nmap 🔍
        2. Check website status 🌐
        3. Check if the website has protection 🛡️
        4. Download all packages ⚠️ [recommended]
        5. Secret Tools 🔑
        6. Exit the tool 🛑
        """)

        choice = input("Enter the option number (1-6): ")

        if choice == "1":
            ip = input("Enter the IP for the port scan: ")
            nmap_scan(ip)
        elif choice == "2":
            check_website_status()
        elif choice == "3":
            target_url = input("Enter the URL to check protection: ")
            check_ddos_protection(target_url)
        elif choice == "4":
            download_all_packages()
        elif choice == "5":
            secret_tools()
        elif choice == "6":
            print("Exiting the tool...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
