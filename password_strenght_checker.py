import re

class PasswordStrengthChecker:
    def __init__(self):
        self.criteria = [
            {"name": "Length", "condition": lambda p: len(p) >= 12, "feedback": "Consider using a longer password for better security."},
            {"name": "Uppercase and Lowercase", "condition": lambda p: any(c.isupper() for c in p) and any(c.islower() for c in p), "feedback": "Mixing uppercase and lowercase letters enhances security."},
            {"name": "Numbers", "condition": lambda p: any(c.isdigit() for c in p), "feedback": "Including numbers adds to the complexity of the password."},
            {"name": "Special Characters", "condition": lambda p: bool(re.match(r'[!@#$%^&*(),.?":{}|<>]', p)), "feedback": "Special characters provide an extra layer of security."},
        ]

    def check_password_strength(self, password):
        score = 0
        feedback = []

        for criterion in self.criteria:
            if criterion["condition"](password):
                score += 1
            else:
                feedback.append(criterion["feedback"])

        if score >= 3:
            return "Strong password! Keep it safe."
        else:
            return "Weak password. " + " ".join(feedback)

def custom_password_check(password, min_length=8, require_special_chars=False):
    if len(password) < min_length:
        return 'Password is too short'
    if require_special_chars and not any(char in '!@#$%^&*()_+' for char in password):
        return 'Password must include special characters'
    return 'Password is strong'

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
