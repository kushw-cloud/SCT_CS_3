import re

class PasswordStrengthChecker:
    # ... (rest of the class remains the same)

def custom_password_check(password, min_length=8, require_special_chars=False):
    # ... (rest of the function remains the same)

def password_score(password):
    score = 0
    if len(password) >= 12:  # longer passwords are stronger
        score += 30
    elif len(password) >= 8:
        score += 20

    if any(char.isdigit() for char in password):
        score += 10
    if any(char.islower() for char in password):
        score += 10
    if any(char.isupper() for char in password):
        score += 10
    if any(char in '!@#$%^&*()_+' for char in password):
        score += 20

    return score

def evaluate_password(password):
    score = password_score(password)
    if score >= 80:
        return 'Strong', score
    elif score >= 50:
        return 'Moderate', score
    else:
        return 'Weak', score

if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    print("Please enter your password below:")

    checker = PasswordStrengthChecker()

    while True:
        password = input("> ")
        if password.lower() == 'exit':
            print("Exiting...")
            break
        strength_feedback = checker.check_password_strength(password)
        custom_feedback = custom_password_check(password, min_length=10, require_special_chars=True)
        password_evaluation, score = evaluate_password(password)
        print(f"Standard check: {strength_feedback}")
        print(f"Custom check: {custom_feedback}")
        print(f"Password evaluation: {password_evaluation} (Score: {score}/100)")
