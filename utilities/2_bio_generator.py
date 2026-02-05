name = input('Name: ')
profession = input('Profession: ' )
passion = input('Passion: ')
emoji = input('Emoji: ')
website = input('Website: ')

layout_1 = f"{emoji} {name} | {profession}\n💡 {passion}\n🔗 {website}"
layout_2 = f"- {emoji} {name}\n- {profession}\n- {passion}\n- {website}"

print(f"Layout 1:\n{layout_1}\nLayout 2\n{layout_2}")

user_preference = input("\nWhich layout do you prefer (1 or 2)? ")

if user_preference == '1':
    layout = layout_1
    print("layout 1 selected")
else:
    layout = layout_2
    print("layout 2 selected")

file_save = input("Do you want to save it in a '.txt' file (yes/No)? ")

if file_save == 'yes':
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, 'w', encoding="utf-8") as f: f.write(layout)
    print("Layout is save as a .txt file")