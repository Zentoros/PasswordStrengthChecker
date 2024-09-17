import re

def check_password_strength(password):
    # Initialize strength levels
    strength = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "numbers": False,
        "special_characters": False
    }

    # Check for minimum length
    if len(password) >= 8:
        strength["length"] = True

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength["uppercase"] = True

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength["lowercase"] = True

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength["numbers"] = True

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength["special_characters"] = True

    # Calculate the strength score
    score = sum(strength.values())

    # Determine the password strength
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    elif score == 5:
        return "Strong"

# Main program
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"The strength of your password is: {strength}")

