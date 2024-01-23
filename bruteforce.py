import os
import subprocess
from termcolor import cprint
import time

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    header = """
 ███████████  ████                                 
░░███░░░░░███░░███                                 
 ░███    ░███ ░███  █████ ████  ██████             
 ░██████████  ░███ ░░███ ░███  ███░░███            
 ░███░░░░░███ ░███  ░███ ░███ ░███████             
 ░███    ░███ ░███  ░███ ░███ ░███░░░              
 ███████████  █████ ░░████████░░██████             
░░░░░░░░░░░  ░░░░░   ░░░░░░░░  ░░░░░░              



 ███████████                █████                  
░░███░░░░░███              ░░███                   
 ░███    ░███  ██████    ███████   ███████  ██████ 
 ░██████████  ░░░░░███  ███░░███  ███░░███ ███░░███
 ░███░░░░░███  ███████ ░███ ░███ ░███ ░███░███████ 
 ░███    ░███ ███░░███ ░███ ░███ ░███ ░███░███░░░  
 ███████████ ░░████████░░████████░░███████░░██████ 
░░░░░░░░░░░   ░░░░░░░░  ░░░░░░░░  ░░░░░███ ░░░░░░  
                                  ███ ░███         
                                 ░░██████          
                                  ░░░░░░           
"""
    cprint(header, 'cyan')

def print_details():
  details = """
\033[1;32m╭──────────────────────────────────────╮
│           \033[1;36m🚀 TOOL DETAILS 🚀\033[1;32m         │
╰──────────────────────────────────────╯
\033[1;37m\033[34mAuthor:\033[0m      thisizasif
\033[1;37m\033[34mGitHub:\033[0m      @thisizasif
\033[1;37m\033[34mTelegram:\033[0m    @thisizasif
\033[1;37m\033[34mVersion:\033[0m     1.1.0
\033[1;37m\033[34mLicense:\033[0m     MIT
\033[1;37m\033[34mDescription:\033[0m Bruteforce tool
"""
  print(details)

def print_menu_options():
    cprint("\n\033[94mBRUTE-FORCE MENU\033[0m", 'yellow')
    time.sleep(0.2)
    print("1 - Brute force a PDF file")
    time.sleep(0.2)
    print("2 - Brute force a ZIP file")
    time.sleep(0.2)

def main():
    clear_terminal()
    print_header()
    print_details()

    while True:
        print_menu_options()
        time.sleep(0.2)

        choice = input("Enter your choice (): ")

        if choice == '1':
            clear_terminal()
            print_header()
            print_details()
            print("\033[94mGeting into PDF Bruteforce...\033[0m")
            time.sleep(2)
            subprocess.run(['python', 'pdflock.py'])
            break
        elif choice == '2':
            clear_terminal()
            print_header()
            print_details()
            print("\033[94mGetting into ZIP Bruteforce...\033[0m")
            time.sleep(2)
            subprocess.run(['python', 'ziplock.py'])
            break
        else:
            print("\033[91mInvalid choice. Please enter a valid option.\033[0m")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
