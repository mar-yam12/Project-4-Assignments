import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def rate_password(password):
    length = len(password)
    score = 0

    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if length >= 12 and score == 4:
        return "💪 Strong"
    elif length >= 8 and score >= 3:
        return "👍 Medium"
    else:
        return "⚠️ Weak"

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print("Your generated password is:", password)
            print("Password strength:", rate_password(password))
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == '__main__':
    main()
