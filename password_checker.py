import re
import random
import string

COMMON_PASSWORDS = ["123456", "password", "qwerty", "admin", "letmein"]

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "@$!%*?&#"
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return "Very Weak ❌", ["Password is too common."], None

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[@$!%*?&#]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if score <= 2:
        strength = "Weak ❌"
        suggestion = generate_strong_password()
    elif score <= 4:
        strength = "Medium ⚠️"
        suggestion = generate_strong_password()
    else:
        strength = "Strong ✅"
        suggestion = None

    return strength, feedback, suggestion

password = input("Enter your password: ")
strength, feedback, suggestion = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if feedback:
    print("Improvements:")
    for item in feedback:
        print(f"- {item}")

if suggestion:
    print(f"\nSuggested Strong Password: {suggestion}")
