def age_conversion():

    age = float(input("Enter your age: "))

    def convert_the_age(age):
        total_days = int(age * 365.25)
        total_hours = int(total_days * 24)
        total_minutes = int(total_hours * 60)

        return f'You are apporximately:\n- {total_days:,} days old\n- {total_hours:,} hours old\n- {total_minutes:,} minutes old'

    return(convert_the_age(age))

while True:
    run = input("Do you want to try the age converter?(y/n) ").strip().lower()
    if run == 'y':
        print(age_conversion())
    else:
        print('Good Bye!!')
        break
    