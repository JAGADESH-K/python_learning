def encription(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base 
            result += chr(shifted)
        else: result += char
    
    return result

def decription(message, key):
    return encription(message, -key)

choice = input("For Encription enter (E) and for Decription (D): ").lower().strip()
message = input("Enter the message: ").strip()
try:
    key = int(input("Enter a key (1-25): "))   
except ValueError:
    print("Enter a number between 1 to 25")

if choice == 'e':
    encripted_message = encription(message, key)
    print(f"The encripted message is:\n{encripted_message}")
elif choice == 'd':
    decripted_message = decription(message, key)
    print(f"The decripted message is:\n{decripted_message}")
else: print("Enter a valid choice.")