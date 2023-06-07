import string
import random

def generate_password(length, uppercase, lowercase, digits, symbols):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if len(characters) == 0:
        print("Error: At least one character type must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password_length = int(input("password length: "))
include_uppercase = True
include_lowercase = True
include_digits = True
include_symbols = True

generated_password = generate_password(password_length, include_uppercase, include_lowercase, include_digits, include_symbols)
if generated_password:
    print("Generated Password:", generated_password)
    