🔐 Python Password Generator & Encrypter
![alt text](https://img.shields.io/badge/Python-3.x-blue.svg)
![alt text](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![alt text](https://img.shields.io/badge/Status-Active-brightgreen.svg)
A robust desktop application built with Python and Tkinter that serves two main purposes: generating secure, randomized passwords and encrypting text using a unique, date-dependent algorithm. The interface is styled with ttkthemes for a modern "Ubuntu" look.
![alt text](path/to/your/screenshot.png)

(Please upload your screenshot to the repository and update this path)
📑 Table of Contents
Features
Prerequisites
Installation
How to Use
Generating Passwords
Encryption & Decryption
Technical Architecture
Author
✨ Features
GUI Interface: Clean, user-friendly interface using the Ubuntu theme.
Customizable Security:
Weak: Lowercase letters only.
Normal: Mixed Uppercase and Lowercase letters.
Strong: Full spectrum (Uppercase, Lowercase, Numbers, and Special Symbols).
Variable Length: Dropdown support for password lengths between 5 and 9 characters.
Dynamic Encryption: A custom Caesar-cipher implementation where the "Shift Key" is calculated automatically based on the current calendar date.
Clipboard Integration: One-click buttons to copy results instantly.
⚙️ Prerequisites
To run this application, you need:
Python 3.x installed on your system.
The ttkthemes library for styling.
🛠️ Installation
Clone the Repository
code
Bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
Install Dependencies
Use pip to install the required theme package:
code
Bash
pip install ttkthemes
Run the Application
code
Bash
python main.py
📖 How to Use
Generating Passwords
Set Length: Locate the dropdown menu next to "Length" and select your desired character count (e.g., 6, 8, etc.).
Select Complexity: Choose a radio button:
Weak: Good for PINs or non-critical local accounts.
Normal: Standard mixed-case passwords.
Strong: High-security passwords with symbols and numbers.
Generate: Click the Generate button. The password will appear in the top text field.
Copy: Click the top Copy button to save the password to your clipboard.
Encryption & Decryption
This tool uses a symmetric encryption method based on the current date.
Encrypt Text:
Type or paste text into the top "Password" field (or generate a random one).
Click the Encrypt button.
The scrambled text will appear in the bottom "Encrypt" field.
Decrypt Text:
Paste the encrypted string into the bottom "Encrypt" field.
Click the Decrypt button.
The original text will appear in the top field.
⚠️ Important Note on Encryption:
The encryption key is derived from today's date (Day + Month + 2).
If you encrypt a password today, you must decrypt it on a day that yields the same key calculation, or the decryption will result in gibberish. This adds a layer of time-based security/obfuscation.
🧠 Technical Architecture
The Character Set
The application uses a custom character set of 72 characters for generation and shifting:
code
Python
digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
The "Date-Key" Algorithm
Unlike standard static keys, this program calculates the shift offset dynamically:
code
Python
x = datetime.datetime.now()
key = (int(day) + int(month)) + 2
Example: On January 14th, the Key is (14 + 1) + 2 = 17.
The Cipher Logic
The encryption iterates through the string and shifts the index of each character by the key, wrapping around using modulo 72.
Encryption: NewChar = Index + Key
Decryption: OriginalChar = Index - Key
👤 Author
Thanos Katsifis
