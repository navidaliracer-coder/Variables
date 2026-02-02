import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short. Pick at least 4 characters."

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# ---- Main Program ----
length = int(input("Enter password length: "))
print("Generated password:", generate_password(length))