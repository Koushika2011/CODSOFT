
#PASSWORD GENERATOR

import random
import string
def generate_password(length=8, use_uppercase=True, use_digits=True, use_special_chars=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation    
    char_set = lower    
    if use_uppercase:
        char_set += upper
    if use_digits:
        char_set += digits
    if use_special_chars:
        char_set += special    
    password = [
        random.choice(lower),
        random.choice(upper) if use_uppercase else '',
        random.choice(digits) if use_digits else '',
        random.choice(special) if use_special_chars else ''
    ]
    if len(password) < length:
        password += random.choices(char_set, k=length - len(password))    
    random.shuffle(password)
    return ''.join(password[:length])
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase=input("Include lowercase letters? (y/n):").lower()=='y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print("Generated password:", password)
