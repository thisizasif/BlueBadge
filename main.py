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
    \033[94mREPO DETAILS\033[0m
    \033[96mAuthor:\033[0m thisizasif
    \033[96mVersion:\033[0m 1.0.0
    \033[96mDescription:\033[0m Blue-Badge pdf Decryption Tool.
    \033[96mLicense:\033[0m MIT
    \033[96mGitHub:\033[0m https://github.com/thisizasif/BlueBadge
    """
    print(details)

def print_menu_options():
    cprint("\n\033[94mBLUE-BADGE MENU\033[0m", 'yellow')
    time.sleep(0.5)
    print("1 - Generate Word-List")
    time.sleep(0.5)
    print("2 - Unlock-Pdf")
    time.sleep(0.5)

def main():
    clear_terminal()
    print_header()
    print_details()

    while True:
        print_menu_options()
        time.sleep(0.5)

        choice = input("Enter your choice (): ")

        if choice == '1':
            clear_terminal()
            print_header()
            print_details()
            print("\033[94mGeting into Word-List...\033[0m")
            time.sleep(2)
            subprocess.run(['python', 'Wordlist.py'])
            break
        elif choice == '2':
            clear_terminal()
            print_header()
            print_details()
            print("\033[94mGetting into PDF...\033[0m")
            time.sleep(2)
            subprocess.run(['python', 'unlockpdf.py'])
            break
        else:
            print("\033[91mInvalid choice. Please enter a valid option.\033[0m")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
