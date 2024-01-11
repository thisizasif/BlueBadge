import itertools
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_permutations(input_str):
    perms = list(itertools.permutations(input_str))
    total_permutations = len(perms)

    print(f"\033[1;32mGenerating permutations... (Total: {total_permutations})\033[0m")

    with open('BlueBadge.txt', 'w') as file:
        for i, perm in enumerate(perms, start=1):
            password = ''.join(perm)
            file.write(password + '\n')
            print(f"\033[1;36mGenerated password {i}/{total_permutations}: {password}\033[0m", end='\r')

    print(f"\n\033[1;32mPermutations saved to BlueBadge.txt.\033[0m")

def main():
    clear_terminal()
  print("\033[1;33m###############################################\033[0m")
  print("\033[1;33m#                                             #\033[0m")
  print("\033[1;33m#        [ Blue Badge ]              #\033[0m")
  print("\033[1;33m#               Version: 1.0.0               #\033[0m")
  print("\033[1;33m#                 Author: Thisizasif          #\033[0m")
  print("\033[1;33m#                                             #\033[0m")
  print("\033[1;33m###############################################\033[0m")
  print("\n")

    

    input_str = input("\033[1;32mEnter the input: \033[0m")
    generate_permutations(input_str)

    input("\033[1;36mPress Enter to continue...\033[0m")
    clear_terminal()

if __name__ == "__main__":
    main()
