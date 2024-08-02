import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    all_characters = lower + upper + digits + special
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
