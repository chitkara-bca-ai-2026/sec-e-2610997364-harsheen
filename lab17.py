students = {
    "101": {"Name": "Aman", "Marks": [85, 90, 78]},
    "102": {"Name": "Simran", "Marks": [88, 76, 92]},
    "103": {"Name": "Rahul", "Marks": [70, 80, 75]}
}

def calculate_results(marks):
    total = sum(marks)
    average = total / 3
    return total, average

def display_student(roll, student):
    total, average = calculate_results(student["Marks"])

    print("\nRoll Number:", roll)
    print("Name:", student["Name"])
    print("Marks:", student["Marks"])
    print("Total:", total)
    print("Average:", average)

def add_student(records, roll, name, marks):
    if roll in records:
        print("Error! Roll number already exists.")
    else:
        records[roll] = {
            "Name": name,
            "Marks": marks
        }
        print("Student added successfully!")

while True:
    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(students) == 0:
            print("No student records found.")
        else:
            for roll, student in students.items():
                display_student(roll, student)

    elif choice == "2":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        marks = []
        for i in range(3):
            mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
            marks.append(mark)

        add_student(students, roll, name, marks)

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")

        student = students.get(roll)

        if student:
            display_student(roll, student)
        else:
            print("Student not found!")

    elif choice == "4":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")