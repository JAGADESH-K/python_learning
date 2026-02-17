import csv
import os

FILENAME = "contacts.csv"

if (not os.path.exists(FILENAME)) or os.path.getsize(FILENAME) == 0:
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f) 
        writer.writerow(['Name', 'Phone', 'Email'])

def add_contact():
    name = input("Enter the name: ").strip()
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()

    # Check for duplicates
    with open(FILENAME, 'r', newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Name already exits")
                return
            
    with open(FILENAME, 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added.")

def view_contacts():
    with open(FILENAME, 'r', newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows) < 1: 
            print("No contacts available!")
            return
        print("\n Your contacts: \n")
        for row in rows[1:]:
            print(f"🧑 {row[0]} | 🤙 {row[1]} | 📧 {row[2]}\n")
    return

def search_contact(name_to_search):
    #name_to_search = input("Enter the contact name: ").strip().lower()
    found = False

    with open(FILENAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for contact in reader:
            if name_to_search in contact["Name"].lower():
                print("\nMatched contact: ")
                print(f'\n🧑 {contact["Name"]} | 🤙 {contact["Phone"]} | 📧 {contact["Email"]}\n')
                found = True
                return found
            
    if not found:
        print("No match found")
        return found
    
def delete_contact():
    contact_name = input("Enter the contact name: ").strip().lower()
    found = search_contact(contact_name)
    if found:
        UPDATED_FILE = "updated_contacts.csv"
        with open(FILENAME, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            updated_contacts = [contact for contact in reader if contact_name.lower() != contact[0].lower()]
                
        with open(UPDATED_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(updated_contacts)
        
        os.remove(FILENAME)
        os.rename(UPDATED_FILE, FILENAME)

        print("\nContact removed\n")
        return
    else: 
        print("Contact not found")
        return


def update_contact():
    contact_name = input("Enter the contact name to update: ").strip().lower()
    UPDATED_FILE = "updated_contacts.csv"
    found = False
    with open(FILENAME, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for contact in reader: 
            if contact_name == contact[0].lower():
                new_name = input("Enter the updated name: ")
                new_phone = input("Enter the updated phone number: ")
                new_email = input("Enter the updated email: ")
                with open(UPDATED_FILE, 'a', newline='', encoding='utf-8') as uf:
                    writer = csv.writer(uf)
                    writer.writerow([new_name, new_phone, new_email])
                    found = True
            else: 
                with open(UPDATED_FILE, 'a', newline='', encoding='utf-8') as uf:
                    writer = csv.writer(uf)
                    writer.writerow([contact[0], contact[1], contact[2]])
    if found:
        os.remove(FILENAME)
        os.rename(UPDATED_FILE, FILENAME)
    else: 
        os.remove(UPDATED_FILE)
        print("Contact not found")
    return

def main():
    while True:
        print("\n--- Opening your contact book ---\n")
        print("Enter 1 to add a contact.")
        print("Enter 2 to view the contacts.")
        print("Enter 3 to search for a contact.")
        print("Enter 4 to delete the contact.")
        print("Enter 5 to update the contact.")
        print("Enter 6 to exit.")

        choise = input("Enter your choise (1-6): ").strip()

        if choise == "1": add_contact()
        elif choise == "2": view_contacts()
        elif choise == "3": search_contact(input("Enter the contact name: ").strip().lower())
        elif choise == "4": delete_contact()
        elif choise == "5": update_contact()
        elif choise == "6": break
        else: print("Please enter a valid number.")

    
if __name__ == "__main__":
    main()
        