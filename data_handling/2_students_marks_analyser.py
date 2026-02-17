def students_report():
    students = {}

    while True:
        name = input("Enter the student name or 'done' to exit: ").strip()
        if name.lower() == "done": break
        if name in students: 
            print("Name already exits")
            continue

        try: 
            score = float(input(f"Enter the {name}'s score: "))
            if score < 0: raise ValueError("Enter the valid number")
        except ValueError: print("Enter the valid number") 
        
        students[name] = score
    return students

def marks_analyser(students: dict):
    marks = list(students.values())
    maximum = max(marks)
    minimun = min(marks)
    average = sum(marks) / len(marks)
    topper = [name for name, mark in students.items() if mark == maximum]

    print(f"\n[-][-][-] Students report [-][-][-]\n")
    print(f"Total students are {len(marks)}.\n")
    print(f"Highest mark is {maximum}.\n")
    print(f"Lowest mark is {minimun}.\n")
    print(f"Average mark is {average:.2f}.\n")
    print(f"Top score is {maximum} by {', '.join(topper)}\n")
    print('-=-' * 10)
    print("\nStudent marks: ")
    for student in students:
        print(f"- {student}: {students[student]}")

    return

report = students_report()
marks_analyser(report)

        
