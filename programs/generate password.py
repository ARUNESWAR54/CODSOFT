import random
import string

def generate_password(length=12):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the list
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Example usage
password = generate_password(12)  # You can specify the length of the password
print(f"Generated password: {password}")
