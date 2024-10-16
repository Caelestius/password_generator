import random
import string

def generate_password(length, use_upper, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the password length: "))
    use_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_upper, use_numbers, use_symbols)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    password_generator()
