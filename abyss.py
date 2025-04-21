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
    return text  # Remove multicolor effect

# Function to show the initial banner
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

# Function to show "Created by Crowley" and two options
def show_creator_message():
    clear_screen()
    print("⚠️ Creator's message: This tool should be used with caution. I will not be responsible for any illegal actions.")
    print("\n")
    print("Created by: crowley")
    print("\n")
    print("(1) Continue")
    print("(2) Go back")
    return input("Enter your choice: ")

# Function to ask if user wants to continue or go back
def ask_continue_or_back():
    choice = show_creator_message()
    if choice == "1":
        return True
    elif choice == "2":
        return False
    else:
        print("Invalid option, returning to the main menu.")
        return False

# Function to perform stress testing (real HTTP DoS)
def stress_test():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        print("🚨 Starting a Stress Test on the target server!")
        ip = input("Enter the IP address of the target: ")
        print(f"Sending heavy traffic to {ip}. Be careful, only use this in controlled environments!")
        
        # Example of a real DoS using Python's socket
        try:
            while True:
                s = subprocess.run(f"curl {ip} --silent --output /dev/null", shell=True)
                print(f"Sending request to {ip}")
        except KeyboardInterrupt:
            print("\nStress Test stopped!")
            input("\nPress Enter to return to the menu...")

# Function to install all available packages in Termux (real)
def install_all_packages():
    if ask_continue_or_back():
        clear_screen()  # Clean screen before performing the action
        print("⚠️ WARNING: You are about to install all available packages in Termux.")
        print("This may take a long time and consume a lot of space!")

        # Comando para habilitar repositorios (si aún no lo has hecho)
        subprocess.run("pkg update", shell=True)
        subprocess.run("pkg upgrade", shell=True)
        subprocess.run("pkg install unstable-repo", shell=True)
        subprocess.run("pkg install x11-repo", shell=True)
        subprocess.run("pkg install science-repo", shell=True)
        subprocess.run("pkg install root-repo", shell=True)
        subprocess.run("pkg install games-repo", shell=True)

        # Instalar todos los paquetes disponibles usando apt
        subprocess.run("apt update", shell=True)
        subprocess.run("apt upgrade", shell=True)
        print("Instalando todos los paquetes con apt...")
        subprocess.run("apt list --installed | awk -F/ '{print $1}' | tr '\n' ' ' | xargs apt install", shell=True)

        # Instalar todos los paquetes disponibles usando pkg
        subprocess.run("pkg update", shell=True)
        subprocess.run("pkg upgrade", shell=True)
        print("Instalando todos los paquetes con pkg...")
        subprocess.run("pkg list-all | awk '{print $1}' | tr '\n' ' ' | xargs pkg install", shell=True)

        # Instalar todos los paquetes de Python usando pip
        subprocess.run("pip install --upgrade pip", shell=True)
        print("Instalando todos los paquetes con pip...")
        subprocess.run("pip list --outdated | awk '{print $1}' | tr '\n' ' ' | xargs pip install", shell=True)
        
        print("\nAll packages installed!")
        input("\nPress Enter to return to the menu...")

# Main menu
def main():
    show_banner()

    while True:
        clear_screen()
        print("""
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
        """)

        choice = input("Enter the option number (1-12): ")

        # Adding the secret option functionality
        if choice == "11":
            password = input("Enter the secret password: ")
            if password == "crowley123":  # Secret password to unlock the option
                secret_option()
            else:
                print("Invalid password. Access denied.")
                input("\nPress Enter to return to the menu...")

        elif choice == "1":
            gather_network_info()
        elif choice == "2":
            check_website_status()
        elif choice == "3":
            stealth_mode()
        elif choice == "4":
            ip = input("Enter the IP for the port scan: ")
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
            print("Exiting the tool...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
