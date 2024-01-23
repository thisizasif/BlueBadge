
<h1 align="center">
  <br>
  <a href="http://thisizasif.blogspot.com/"><img src="https://github.com/thisizasif/BlueBadge/assets/68771679/7ab73a37-f577-40d4-ae37-cae899b1798a" alt="Thisizasif" width="200"></a>
  <br>
  Blue-Badge
  <br>
</h1>


<p align="center">
    <img src="https://badge.fury.io/js/thisizasif"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/thisizasif/BlueBadge"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/thisizasif@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/thisizasif">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#Installation">Installation</a> •
  <a href="#Support">Support</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![screenshot]![IMG_20240112_180159 1](https://github.com/thisizasif/BlueBadge/assets/68771679/1388b131-25e2-4aef-957b-53b1644351a5)



## Key Features

- **Word List Generation:** The tool can generate permutations of input strings to create a word list for password cracking.

- **PDF Decryption:** Utilizes the `pikepdf` library to attempt to decrypt a PDF file using passwords from the generated word list.

## Installation

Ensure a smooth setup by installing the necessary dependencies. In your Termux environment, run the following commands:


```bash
apt update -y
```

```bash
apt upgrade -y
```

```bash
pkg install git
```

```bash
pkg install python 
```

```bash
pip3 install termcolor
```

```bash
pkg install qpdf
```

```bash
pkg install libxml2 libxslt
```

```bash
pip3 install tqdm
```

```bash
pip3 install pikepdf
```

optional
```bash
pip3 install Pillow Deprecated packaging lxml wrapt
```
```bash
pip install wrapt==1.16.0 deprecated==1.2.14 lxml==5.1.0 packaging==23.2 pillow==10.2.0 pikepdf==8.11.2 termcolor==2.4.0 tqdm==4.66.1
```
## How To Use

To clone and run BlueBadge, you'll need to follow these steps From your command line:

# Clone this repository
```bash
$ git clone https://github.com/thisizasif/BlueBadge.git
```

# Go into the repository
```bash
$ cd BlueBadge
```

# Run the tool
```bash
$ python3 main.py
```

> **Tip:**
For optimal functionality of BlueBadge's `unlockpdf.py` script, follow these steps:

1. **Rename PDF File:** Ensure your PDF file is named `bluebadge.pdf`.
   
2. **Move/Copy to BlueBadge Directory:** Place the renamed `bluebadge.pdf` in the BlueBadge directory.

**Important:** Failure to adhere to these instructions might result in `unlockpdf.py` not working as expected.

## Support

<a href="https://www.buymeacoffee.com/thisizasif" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/thisizasif">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## You may also like...

- [thisizasif]() - 
- [thisizasif]() - 

## License

MIT

---

> GitHub [@thisizasif](https://github.com/thisizasif) &nbsp;&middot;&nbsp;
> Twitter [@thisizasif](https://twitter.com/thisixasif)

## Disclaimer

⚠️ **Disclaimer: Hacking Without Permission is Illegal**

This tool is strictly educational, focusing on cyber-security, ethical hacking, and penetration testing. The tool is designed to facilitate learning and understanding in Cyber-Security, empowering individuals to defend themselves against real hackers.

Remember, always act responsibly and within legal boundaries when it comes to exploring and applying your knowledge in the field of cyber-security.
