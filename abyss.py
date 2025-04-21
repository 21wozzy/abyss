import os
import time
import subprocess
import sys

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
def scan_ports():
    ip = input("Enter the IP for the port scan: ")
    print(f"Scanning ports of {ip} with Nmap...")
    subprocess.run(f"nmap {ip}", shell=True)
    input("\nPress Enter to return to the menu...")

# Function for checking website status
def check_website_status():
    url = input("Enter the website URL (e.g., https://example.com): ")
    response = subprocess.run(f"curl -Is {url} | head -n 1", shell=True, capture_output=True, text=True)
    print(f"Status: {response.stdout}")
    input("\nPress Enter to return to the menu...")

# Function for making a strong HTTP request
def make_http_request():
    url = input("Enter the URL for the HTTP request: ")
    method = input("Enter the HTTP method (GET, POST, etc.): ")
    headers = input("Enter any additional headers (optional): ")
    print(f"Making a {method} request to {url}...")
    subprocess.run(f"curl -X {method} {url} -H '{headers}'", shell=True)
    input("\nPress Enter to return to the menu...")

# Function for checking if a website has protection
def check_website_protection():
    url = input("Enter the website URL to check protection: ")
    print(f"Checking DDoS protection for {url}...")
    subprocess.run(f"curl -I {url}", shell=True)
    input("\nPress Enter to return to the menu...")

# Function for attacking an IP and port
def attack_ip_and_port():
    ip = input("Enter the target IP: ")
    port = input("Enter the target port: ")
    print(f"Attacking {ip} on port {port}...")
    subprocess.run(f"hydra -l admin -P /path/to/passwordlist.txt {ip} {port}", shell=True)
    input("\nPress Enter to return to the menu...")

# Function for scanning vulnerabilities
def scan_vulnerabilities():
    url = input("Enter the URL to scan for vulnerabilities: ")
    print(f"Scanning {url} for vulnerabilities...")
    subprocess.run(f"nikto -h {url}", shell=True)
    input("\nPress Enter to return to the menu...")

# Function for scanning DNS and subdomains
def scan_dns_and_subdomains():
    domain = input("Enter the domain to scan for DNS and subdomains: ")
    print(f"Scanning {domain} for subdomains...")
    subprocess.run(f"amass enum -d {domain}", shell=True)
    input("\nPress Enter to return to the menu...")

# Function to download all packages in Termux (apt, pip)
def install_packages():
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
    6. **ClamAV**: Anti-virus tool. It helps scan files for viruses.
    7. **SSL Labs**: Analyzes SSL certificates of a website.
    8. **Wireshark**: Packet analyzer for inspecting network traffic.
    
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
    6. ClamAV - Virus scanner
    7. SSL Labs - SSL certificate information
    8. Wireshark - Network protocol analyzer
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
    elif tool_choice == "6":
        print("Running ClamAV to scan for viruses...")
        subprocess.run("clamav -r /path/to/scan", shell=True)
    elif tool_choice == "7":
        url = input("Enter the URL for SSL certificate info: ")
        subprocess.run(f"ssllabs-scan {url}", shell=True)
    elif tool_choice == "8":
        print("Starting Wireshark for packet capture...")
        subprocess.run("wireshark", shell=True)
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
        [1] Scan ports with Nmap 🔍
        [2] Check website status 🌐
        [3] Make a strong HTTP request ⚡
        [4] Check if the website has protection 🛡️
        [5] Attack an IP and port 💥
        [6] Scan for vulnerabilities 🕵️‍♂️
        [7] Scan DNS and subdomains 🌐
        [8] Download all packages ⚠️ [recommended]
        [9] Secret Tools 🔑
        [10] Exit the tool 🛑
        """)

        choice = input("Enter the option number (1-10): ")

        if choice == "1":
            scan_ports()
        elif choice == "2":
            check_website_status()
        elif choice == "3":
            make_http_request()
        elif choice == "4":
            check_website_protection()
        elif choice == "5":
            attack_ip_and_port()
        elif choice == "6":
            scan_vulnerabilities()
        elif choice == "7":
            scan_dns_and_subdomains()
        elif choice == "8":
            install_packages()
        elif choice == "9":
            secret_tools()
        elif choice == "10":
            print("Exiting the tool...")
            sys.exit()
        else:
            print("Invalid option. Please try again.")
            input("\nPress Enter to continue...")
