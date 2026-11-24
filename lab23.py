import os

filename = "student_marks.txt"
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("Aman,85\n")
        file.write("Simran,90\n")
        file.write("Rahul,78\n")

def store_student(filename, name, marks):
    with open(filename, "a") as file:
        file.write(name + "," + str(marks) + "\n")

    print("Student record saved successfully!")

def display_records(filename):
    if not os.path.exists(filename):
        print("No records found!")
        return

    total = 0
    count = 0

    print("\n===== STUDENT RECORDS =====")
    print("Name\tMarks")

    with open(filename, "r") as file:
        for line in file:
            name, marks = line.strip().split(",")
            marks = int(marks)

            print(name, "\t", marks)

            total += marks
            count += 1

    if count > 0:
        average = total / count
        print("\nTotal Students:", count)
        print("Total Marks:", total)
        print("Class Average: {:.2f}".format(average))
    else:
        print("No student records found!")

# Main menu
while True:
    print("\n===== STUDENT MARKS MANAGEMENT =====")
    print("1. Add & Store Student Marks")
    print("2. Display Records & Class Average")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))

        if 0 <= marks <= 100:
            store_student(filename, name, marks)
        else:
            print("Please enter marks between 0 and 100.")

    elif choice == "2":
        display_records(filename)

    elif choice == "3":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")