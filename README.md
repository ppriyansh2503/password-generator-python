# 🔐 Advanced Password Generator Using Python

A feature-rich password generator built with Python to create strong and customizable passwords.

## 📌 About the Project

The Advanced Password Generator helps users generate passwords with different character combinations. It also includes password strength evaluation and generation history.

This project demonstrates Python functions, loops, conditional statements, exception handling, secure random generation, file handling, and JSON operations.

## ✨ Features

- Generate passwords from 8 to 128 characters.
- Include uppercase and lowercase letters.
- Include numbers and special characters.
- Exclude similar-looking characters such as `I`, `l`, `1`, `O`, and `0`.
- Evaluate password strength.
- Receive suggestions to improve password strength.
- View recent password generation history.
- Save generation metadata in a JSON file.
- Uses Python's `secrets` module for secure password generation.
- Does not store generated passwords in the history file.

## 🛠️ Technologies Used

- Python 3
- `secrets`
- `string`
- `re`
- `json`
- `os`
- `datetime`

## 📂 Project Structure

```text
password-generator-python/
├── password_generator.py
└── README.md
```

The `password_history.json` file is created automatically when generation metadata is saved.

## ⚙️ Requirements

- Python 3.8 or later
- No external packages required

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/sweetykumari9670-code/password-generator-python.git
   ```

2. Open the project directory:

   ```bash
   cd password-generator-python
   ```

3. Run the Python program:

   ```bash
   python3 password_generator.py
   ```

## 💻 How to Use

1. Select an option from the main menu.
2. Enter the desired password length.
3. Choose the character types you want.
4. Decide whether to exclude similar-looking characters.
5. View your generated password and its strength.
6. Use the history option to view recent generation metadata.

You can also check the strength of an existing password.

## 🔒 Security Notes

- Passwords are generated using Python's `secrets` module.
- The history file stores metadata, not the actual generated passwords.
- Password strength evaluation is a basic educational check and does not guarantee protection against every attack.
- Avoid sharing generated passwords or committing passwords and other secrets to GitHub.

## 🎯 Learning Outcomes

This project provides practical experience with:

- Functions and modular programming
- Loops and conditional logic
- Input validation
- Exception handling
- Secure random number generation
- Regular expressions
- JSON file operations

## 👨‍💻 Author

Created as a Python programming project.

## 📄 License

This project is available for educational and personal learning purposes.
