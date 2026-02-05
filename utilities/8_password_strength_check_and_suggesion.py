import string
import random
import getpass

def password_strength_check(password):
    issues = []
    if len(password) < 8: issues.append("Password must be 8 char or more")
    if not any(c.islower() for c in password): issues.append("Password must contain atleast 1 lower cher")
    if not any(c.isupper() for c in password): issues.append("Password must contain atleast 1 upper cher")
    if not any(c.isdigit() for c in password): issues.append("Password must contain atleast 1 digit")
    if not any(c in string.punctuation for c in password): issues.append("Password must contain atleast 1 special cher")
    else: print("you have strong password")

    return issues

def password_generator(length=12):
    cher = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(cher) for _ in range(length))
        
password = getpass.getpass("Enter your password: \n")
issues = password_strength_check(password)
suggesion = password_generator()

if issues:
    print("Your password is week\n")
    for issue in issues:
        print(f"- {issue}\n")
    print("Suggesing strong password\n")
    print(suggesion)
    

