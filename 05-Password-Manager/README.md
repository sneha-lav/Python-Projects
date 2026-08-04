# Password Vault 🔐

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A command-line password manager built with Python that allows users to securely store and retrieve account credentials using a simple and organized interface. This project focuses on file handling, modular programming, and creating a practical utility application.

---

## Features

- Add new account credentials
- View saved passwords
- Password masking using `getpass`
- File-based data storage
- Input validation
- Modular code organization

---

## Concepts Practiced

- File Handling
- Functions
- Loops
- Modules
- User Input
- Exception Handling
- String Manipulation

---

## Project Structure

```text
05-Password-Manager/
│
├── main.py
├── manager.py
├── passwords.txt
└── README.md
```

---

## How to Run

```bash
cd 05-Password-Manager
py main.py
```

---

## Sample Output

```text
=========================================
          🔐 PASSWORD VAULT
=========================================

1. Add Password
2. View Passwords
3. Exit

Choose an option: 1

Website : github.com
Username: sneha
Password: ********

✅ Password saved successfully!
```

---

## Learning Outcomes

Through this project, I practiced:

- Reading and writing text files
- Organizing code using modules
- Building a menu-driven application
- Managing user input
- Applying basic exception handling

---

## Future Improvements

### v1.1
- [ ] Search passwords by website
- [ ] Delete saved credentials
- [ ] Update existing passwords

### v1.2
- [ ] Generate secure random passwords
- [ ] Password strength checker
- [ ] Copy generated password to clipboard

### v1.3
- [ ] Store passwords using SQLite
- [ ] Encrypt stored passwords
- [ ] Export passwords as CSV

### v2.0
- [ ] Master password authentication
- [ ] Graphical User Interface (GUI) using Tkinter

---

## Credits

Inspired by the **21 Python Projects** series by **Tech With Tim**.