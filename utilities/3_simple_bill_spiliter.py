from functools import wraps

no_of_people = int(input("No of people: "))
people_name = [input("Enter name: ") for _ in range(no_of_people)]
total_bill = int(input("Enter the total amount: "))

def final_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('*' * 10)
        print(func(*args, **kwargs))
        print('*' * 10)
    return wrapper

@final_wrapper
def bill_share_calculation(total_bill, no_of_people, people_name):
    share = total_bill / no_of_people
    shared_bill = ''
    for people in people_name:
        shared_bill += f'{people} owes Rs.{share:.2f}'
        shared_bill = shared_bill.__add__('\n')
    return shared_bill

final_bill = bill_share_calculation(total_bill,no_of_people,people_name)

