import base64
import os

VAULT_FILE = 'vault.txt'

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_specal = any(c in ['!','@','#','$','%','&','*','.',','] for c in password)

    score = sum([length>=8, has_upper, has_digit, has_specal])
    return ['Weak', 'Medium', 'Strong', 'Very Strong'][min(score, 3)]

def add_credentials():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = password_strength(password)
    print(f"\nyour password is {strength}\n")

    line = f"{website} || {username} || {password}"

    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding='utf-8') as f:
        f.write(encoded_line + '\n')    

    print('✅ Credential saved')

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File not found")

    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            decoded_line = decode(line.strip())
            website, username, password = decoded_line.split('||')
            print('----')
            print(f"website: {website}\nusername: {username}\npassword: {password}")

def main():
    while True:
        print("\n**** Offline Security Vault ****")
        print("\nEnter 1 to add credentials")
        print("Enter 2 to view all credentials")
        print("Enter 3 to exit")

        option = input("\nEnter your option: ")

        match option:
            case '1': add_credentials()
            case '2': view_credentials()
            case '3': break
            case _ : "Invalid option"

if __name__ == "__main__":
    main()       
