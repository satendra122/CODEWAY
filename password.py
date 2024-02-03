import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Error: Password length should be greater than zero.")
        else:
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid numerical value for the password length.")