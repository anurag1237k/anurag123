import random
import string

def generate_password(length, use_lower, use_upper, use_digits, use_special):
    characters = ""
    
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:

        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: Select at least one character type!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- User Input Section ---
try:
    length = int(input("Enter password length: "))

    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_lower, use_upper, use_digits, use_special)
    print(f"\nGenerated Password: {password}")

except ValueError:
    print("Please enter a valid number for length.")


