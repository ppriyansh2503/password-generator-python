import secrets
import string
import re
import json
import os
from datetime import datetime

HISTORY_FILE = "password_history.json"


def display_banner():
    print("\n" + "=" * 55)
    print("          ADVANCED PASSWORD GENERATOR")
    print("=" * 55)
    print("Create strong and customizable passwords securely!")
    print("=" * 55)


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (8-128): "))

            if 8 <= length <= 128:
                return length

            print("Please enter a length between 8 and 128.")

        except ValueError:
            print("Invalid input. Enter a number.")


def get_character_options():
    print("\nChoose character types:")
    print("1. Include uppercase letters")
    print("2. Include lowercase letters")
    print("3. Include numbers")
    print("4. Include special characters")

    options = {}

    for option, description in [
        ("1", "Uppercase letters"),
        ("2", "Lowercase letters"),
        ("3", "Numbers"),
        ("4", "Special characters")
    ]:
        while True:
            answer = input(f"{description}? (y/n): ").strip().lower()

            if answer in ("y", "n"):
                options[option] = answer == "y"
                break

            print("Please enter y or n.")

    if not any(options.values()):
        print("No character type selected. Using all character types.")
        options = {key: True for key in ("1", "2", "3", "4")}

    return options


def generate_password(length, options, exclude_similar=False):
    character_groups = []

    if options.get("1"):
        character_groups.append(string.ascii_uppercase)

    if options.get("2"):
        character_groups.append(string.ascii_lowercase)

    if options.get("3"):
        character_groups.append(string.digits)

    if options.get("4"):
        character_groups.append("!@#$%^&*()-_=+[]{};:,.?/")

    if exclude_similar:
        similar = "Il1O0o"
        character_groups = [
            "".join(char for char in group if char not in similar)
            for group in character_groups
        ]
        character_groups = [group for group in character_groups if group]

    if not character_groups:
        raise ValueError("No usable characters selected.")

    all_characters = "".join(character_groups)

    if length < len(character_groups):
        raise ValueError(
            "Password length is too short for selected character types."
        )

    # Guarantee at least one character from each selected group.
    password_characters = [
        secrets.choice(group) for group in character_groups
    ]

    # Fill the remaining positions securely.
    password_characters.extend(
        secrets.choice(all_characters)
        for _ in range(length - len(password_characters))
    )

    # Securely shuffle the generated characters.
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


def save_password_metadata(password_length, strength):
    # Save metadata only, never the actual password.
    entry = {
        "length": password_length,
        "strength": strength,
        "created_at": datetime.now().isoformat(timespec="seconds")
    }

    history = []

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                history = json.load(file)

            if not isinstance(history, list):
                history = []

        except (json.JSONDecodeError, OSError):
            history = []

    history.append(entry)
    history = history[-20:]

    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    except OSError:
        print("Warning: Could not save generation metadata.")


def view_history():
    if not os.path.exists(HISTORY_FILE):
        print("\nNo generation history found.")
        return

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)

        if not history:
            print("\nNo generation history found.")
            return

        print("\n" + "-" * 55)
        print("             GENERATION HISTORY")
        print("-" * 55)

        for index, entry in enumerate(history, start=1):
            print(
                f"{index}. Length: {entry.get('length', 'N/A')} | "
                f"Strength: {entry.get('strength', 'N/A')} | "
                f"Created: {entry.get('created_at', 'N/A')}"
            )

    except (json.JSONDecodeError, OSError):
        print("Unable to read generation history.")


def password_generator_menu():
    while True:
        print("\nMAIN MENU")
        print("1. Generate a password")
        print("2. Check password strength")
        print("3. View generation history")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            length = get_password_length()
            options = get_character_options()

            exclude_similar = (
                input("Exclude similar characters (Il1O0o)? (y/n): ")
                .strip()
                .lower()
                == "y"
            )

            try:
                password = generate_password(
                    length, options, exclude_similar
                )

                strength, feedback = evaluate_password(password)

                print("\n" + "=" * 55)
                print("Generated Password:", password)
                print("Password Length:", len(password))
                print("Password Strength:", strength)
                print("=" * 55)

                if feedback:
                    print("\nSuggestions:")
                    for suggestion in feedback:
                        print("-", suggestion)

                save_password_metadata(len(password), strength)

            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            password = input("Enter a password to evaluate: ")
            strength, feedback = evaluate_password(password)

            print("\nPassword Strength:", strength)

            if feedback:
                print("Suggestions:")
                for suggestion in feedback:
                    print("-", suggestion)
            else:
                print("Your password meets the basic strength checks.")

            print(
                "Note: This is a basic checker, not a guarantee "
                "against password attacks."
            )

        elif choice == "3":
            view_history()

        elif choice == "4":
            print("\nThank you for using Advanced Password Generator!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


def main():
    display_banner()
    password_generator_menu()


if __name__ == "__main__":
    main()
