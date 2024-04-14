import secrets
import string

def generate_password(length, include_digits=True, include_symbols=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_digits, include_symbols)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
