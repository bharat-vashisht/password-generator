import random
import string

def generate_password(length=12, use_special_chars=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ""

    # Ensure the password contains at least one character from each required set
    all_characters = lowercase + uppercase + digits + special_chars
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars) if use_special_chars else random.choice(lowercase)
    ]

    # Fill the remaining length with random choices from all character sets
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)  # Shuffle to avoid predictable sequences

    return ''.join(password)

if __name__ == "__main__":
    password = generate_password(12)
    print("Generated Password:", password)