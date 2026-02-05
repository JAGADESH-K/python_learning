from datetime import date

# name = input("Name: ")
# age = input("Age: ")
# city = input("City: ")
# profession = input("Profession: ")
# hobby = input("Hobby: ")

details = ['Name', 'Age', 'City', 'Profession', 'Hobby']

user_details = {}

for detail in details:
    user_detail = input(f"{detail}: ").strip()
    user_details[detail] = user_detail

print(f"{'*' * 3} \nHello! My name is {user_details['Name']}. I'm {user_details['Age']} years old and live in {user_details['City']}. I work as a {user_details['Profession']} and I absolutely enjoy {user_details['Hobby']} in my free time. Nice to meet you! \nLogged on: {date.today().isoformat()} \n{'*' * 3}")