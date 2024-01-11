import itertools

banner = """
 ███████████  ████                         ███████████                █████                  
░░███░░░░░███░░███                        ░░███░░░░░███              ░░███                   
 ░███    ░███ ░███  █████ ████  ██████     ░███    ░███  ██████    ███████   ███████  ██████ 
 ░██████████  ░███  ░░███ ░███  ███░░███    ░██████████  ░░░░░███  ███░░███  ███░░███ ███░░███
 ░███░░░░░███ ░███  ░███ ░███ ░███████     ░███░░░░░███  ███████ ░███ ░███ ░███ ░███░███████ 
 ░███    ░███ ░███  ░███ ░███ ░███░░░      ░███    ░███ ███░░███ ░███ ░███ ░███ ░███░███░░░  
 ███████████  █████ ░░████████░░██████     ███████████ ░░████████░░████████░░███████░░██████ 
░░░░░░░░░░░  ░░░░░   ░░░░░░░░  ░░░░░░     ░░░░░░░░░░░   ░░░░░░░░  ░░░░░░░░  ░░░░░███ ░░░░░░  
                                                                            ███ ░███         
                                                                           ░░██████          
                                                                            ░░░░░░           
"""

print(banner)

input_str = input("Enter the input: ")

perms = list(itertools.permutations(input_str))
total_permutations = len(perms)

print(f"\nGenerating permutations... (Total: {total_permutations})\n")

with open('BlueBadge.txt', 'w') as file:
    for i, perm in enumerate(perms, start=1):
        password = ''.join(perm)
        file.write(password + '\n')
        print(f"Generated password {i}/{total_permutations}: {password}")

print("\nPermutations saved to BlueBadge.txt.")
