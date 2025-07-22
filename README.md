What it does

Analyzes passwords for length and presence of lowercase, uppercase, digits, and special characters.

Gives live feedback and assigns a strength classification (Weak → Strong). 
GitHub
+3
GitHub
+3
GitHub
+3
GitHub
+1
GitHub
+1

Languages

Primarily Python, but also includes HTML and CSS components (likely for UI). 
GitHub
GitHub

Installation & Usage
While not detailed in the visible README, typical usage likely involves cloning the repo and running the Python script.
# 🔐 Password Strength Checker

A simple Python-based application that checks the strength of a password based on entropy, common password patterns, and length. Built with Tkinter for GUI.

## 📸 GUI Preview

![Password Strength Checker Screenshot](https://github.com/Nocknock01/Password-Strength-Checker/blob/main/screenshot.png)

---

## 🧠 Features

- Calculates password entropy
- Warns against common/weak passwords
- Provides visual feedback (color-coded)
- Easy-to-use GUI with Tkinter

---

## 🛠️ Requirements

- Python 3.x  
- Tkinter (usually pre-installed with Python)

---

## ▶️ How to Run the Code

1. **Clone the Repository:**

```bash
git clone https://github.com/Nocknock01/Password-Strength-Checker.git
cd Password-Strength-Checker
python password_strength_checker.py
Password-Strength-Checker/
├── common_passwords.txt     # List of common passwords
├── password_strength_checker.py  # Main Python script with GUI
├── README.md
└── screenshot.png
