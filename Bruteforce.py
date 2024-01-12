import fitz  # PyMuPDF
from tqdm import tqdm

banner = """
       
"""

print(banner)

# load password list
passwords = [line.strip() for line in open("BlueBadge.txt")]

# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file
        with fitz.open("bluebadge.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", password)
            break
    except Exception as e:
        # wrong password or other exception, just continue in the loop
        continue

