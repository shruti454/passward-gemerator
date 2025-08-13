import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user preferences."""
    char_pool = ""

    if use_letters:
        char_pool += string.ascii_letters  # a-z + A-Z  
    if use_numbers:
        char_pool += string.digits  # 0-9
    if use_symbols:
        char_pool += string.punctuation  # special characters

    if not char_pool:
        raise ValueError("No character set selected. Enable at least one option.")

    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    print("=== Random Password Generator ===")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            return

        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("\nGenerated Password:", password)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
