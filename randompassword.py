import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
    
    if not character_pool:
        print("Error: No character types selected. Please choose at least one.")
        return None
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
    
    if password:
        print(f"Generated Password: {password}")
