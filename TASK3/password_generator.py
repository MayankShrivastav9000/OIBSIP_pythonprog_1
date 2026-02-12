import string
import secrets
import sys

def get_user_preferences():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError
    except ValueError:
        print("Invalid length. Must be a positive integer.")
        sys.exit(1)

    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    char_pool = ""

    if use_lower:
        char_pool += string.ascii_lowercase
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        print("You selected no character types. Password cannot be generated.")
        sys.exit(1)

    return length, char_pool


def generate_password(length, char_pool):
    return ''.join(secrets.choice(char_pool) for _ in range(length))


def main():
    print("=== Secure Password Generator ===")
    length, char_pool = get_user_preferences()
    password = generate_password(length, char_pool)
    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
