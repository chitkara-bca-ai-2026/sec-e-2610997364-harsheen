import csv
import os

filename = "students_data.csv"

if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["RollNo", "Name", "Subject", "Marks"])

        writer.writerow([101, "Aman", "Python", 85])
        writer.writerow([102, "Simran", "Maths", 45])
        writer.writerow([103, "Rahul", "Python", 65])
        writer.writerow([104, "Priya", "Maths", 38])
        writer.writerow([105, "Karan", "Python", 90])

def read_all_students(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        print("\n===== ALL STUDENT RECORDS =====")
        print("RollNo\tName\tSubject\tMarks")

        for row in reader:
            print(row["RollNo"], "\t", row["Name"],
                  "\t", row["Subject"], "\t", row["Marks"])


def filter_students_above_threshold(filename, threshold=50):
    count = 0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        print("\n===== STUDENTS SCORING ABOVE 50 =====")
        print("RollNo\tName\tSubject\tMarks")

        for row in reader:
            if int(row["Marks"]) > threshold:
                print(row["RollNo"], "\t", row["Name"],
                      "\t", row["Subject"], "\t", row["Marks"])
                count += 1

    print("\nTotal Qualified Students:", count)

while True:
    print("\n===== STUDENT MARKS FILTER =====")
    print("1. Display All Students")
    print("2. Filter Marks Above 50")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        read_all_students(filename)

    elif choice == "2":
        filter_students_above_threshold(filename, 50)

    elif choice == "3":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")