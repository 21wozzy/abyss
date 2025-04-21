import os
import time
import subprocess
import sys
import random

# Function to clear the screen
def clear_screen():
    os.system('clear')

# Function to print text with multicolor effect
def multicolor_text(text):
    colors = [
        '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m',
        '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
    ]
    colored_text = ""
    for i, char in enumerate(text):
        color = random.choice(colors)
        colored_text += color + char
    return colored_text + '\033[0m'

# Function to show the initial banner with multicolor effect
def show_banner():
    clear_screen()
    banner = """
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
    """
    print(multicolor_text(banner))
    time.sleep(2)

# Function to show "Created by Crowley" and two options in multicolor
def show_creator_message():
    clear_screen()
    print(multicolor_text("⚠️ Creator's message: This tool should be used with caution. I will not be responsible for any illegal actions."))
    print("\n")
    print(multicolor_text("Created by: crowley"))
    print("\n")
    print(multicolor_text("(1) Continue"))
    print(multicolor_text("(2) Go back"))
    return input(multicolor_text("Enter your choice: "))

# Function to ask if user wants to continue or go back
def ask_continue_or_back():
    choice = show_creator_message()
    if choice == "1":
        return True
    elif choice == "2":
        return False
    else:
        print(multicolor_text("Invalid option, returning to the main menu."))
        return False

# Secret option function
def secret_option():
    clear_screen()
    print(multicolor_text("🔒 Secret Option Unlocked!"))
    print(multicolor_text("This is a highly restricted function. Use it responsibly!"))
    # Do something secret here
    time.sleep(2)
    input(multicolor_text("\nPress Enter to return to the menu..."))

# Function to perform stress testing (real HTTP DoS)
def stress_test():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        print(multicolor_text("🚨 Starting a Stress Test on the target server!"))
        ip = input(multicolor_text("Enter the IP address of the target: "))
        print(multicolor_text(f"Sending heavy traffic to {ip}. Be careful, only use this in controlled environments!"))
        
        # Example of a real DoS using Python's socket
        try:
            while True:
                s = subprocess.run(f"curl {ip} --silent --output /dev/null", shell=True)
                print(f"Sending request to {ip}")
        except KeyboardInterrupt:
            print(multicolor_text("\nStress Test stopped!"))
            input(multicolor_text("\nPress Enter to return to the menu..."))

# Function for advanced vulnerability scanning (Nikto example)
def advanced_vulnerability_scan():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        print(multicolor_text("🕵️‍♂️ Performing advanced vulnerability scan with Nikto!"))
        target = input(multicolor_text("Enter the target URL for vulnerability scan: "))
        subprocess.run(f"nikto -h {target}", shell=True)
        input(multicolor_text("\nPress Enter to return to the menu..."))

# Function to run Metasploit to exploit vulnerabilities
def run_metasploit():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        print(multicolor_text("⚠️ WARNING: This will attempt to exploit vulnerabilities using Metasploit."))
        print(multicolor_text("You must have Metasploit installed on your system."))
        print(multicolor_text("Starting Metasploit..."))
        subprocess.run("msfconsole", shell=True)
        input(multicolor_text("\nPress Enter to return to the menu..."))

# Function to gather network information and host data
def gather_network_info():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        print(multicolor_text("🌐 Gathering network information..."))
        subprocess.run("ifconfig", shell=True)
        subprocess.run("netstat -tuln", shell=True)
        input(multicolor_text("\nPress Enter to return to the menu..."))

# Function to stealth mode (evade detection)
def stealth_mode():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        print(multicolor_text("⛔ Engaging stealth mode: Attempting to avoid detection!"))
        subprocess.run("nmap -sS -O -T0 192.168.1.1", shell=True)  # Example stealth scan
        input(multicolor_text("\nPress Enter to return to the menu..."))

# Function to scan for open ports in stealth mode
def stealth_port_scan():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        ip = input(multicolor_text("Enter the IP for stealth port scan: "))
        subprocess.run(f"nmap -sS {ip}", shell=True)
        input(multicolor_text("\nPress Enter to return to the menu..."))

# Function to check website status with extended info (real)
def check_website_status():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        url = input(multicolor_text("Enter the website URL (e.g., https://example.com): "))
        response = subprocess.run(f"curl -Is {url} | head -n 1", shell=True, capture_output=True, text=True)
        print(multicolor_text(f"Status: {response.stdout}"))
        input(multicolor_text("\nPress Enter to return to the menu..."))

# Function to install all available packages in Termux (real)
def install_all_packages():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        print(multicolor_text("⚠️ WARNING: You are about to install all available packages in Termux."))
        print(multicolor_text("This may take a long time and consume a lot of space!"))
        subprocess.run("pkg update -y && pkg upgrade -y", shell=True)
        subprocess.run("pkg install $(pkg list -a) -y", shell=True)
        subprocess.run("pip install --upgrade pip", shell=True)
        subprocess.run("pip freeze | cut -d = -f 1 | xargs pip install --upgrade", shell=True)
        print(multicolor_text("\nAll packages installed!"))
        input(multicolor_text("\nPress Enter to return to the menu..."))

# Main menu
def main():
    show_banner()

    while True:
        clear_screen()
        print(multicolor_text("""
        Select an option (from lightest to strongest):
        1. 🌐 Gather network info (ifconfig, netstat)
        2. 🔍 Check website status
        3. ⛓️ Stealth mode (evade detection)
        4. 🔌 Scan ports with Nmap
        5. 🔙 Make a strong HTTP request
        6. ⚡ Stress Testing (DoS/DDoS simulation)
        7. 🛡️ Advanced vulnerability scan
        8. 🚪 Scan open ports (manual)
        9. ⚠️ Install all packages in Termux
        10. 🧨 Run Metasploit to exploit vulnerabilities
        11. 🔒 Secret Option (requires a password)
        12. ⛔ Exit the tool
        """))

        choice = input(multicolor_text("Enter the option number (1-12): "))

        # Adding the secret option functionality
        if choice == "11":
            password = input(multicolor_text("Enter the secret password: "))
            if password == "crowley123":  # Secret password to unlock the option
                secret_option()
            else:
                print(multicolor_text("Invalid password. Access denied."))
                input(multicolor_text("\nPress Enter to return to the menu..."))

        elif choice == "1":
            gather_network_info()
        elif choice == "2":
            check_website_status()
        elif choice == "3":
            stealth_mode()
        elif choice == "4":
            ip = input(multicolor_text("Enter the IP for the port scan: "))
            subprocess.run(f"nmap -p- {ip}", shell=True)
        elif choice == "5":
            stress_test()
        elif choice == "6":
            stress_test()
        elif choice == "7":
            advanced_vulnerability_scan()
        elif choice == "8":
            stealth_port_scan()
        elif choice == "9":
            install_all_packages()
        elif choice == "10":
            run_metasploit()
        elif choice == "12":
            print(multicolor_text("Exiting the tool..."))
            sys.exit()
        else:
            print(multicolor_text("Invalid choice. Please try again."))
            input(multicolor_text("\nPress Enter to return to the menu..."))

if __name__ == "__main__":
    main()
