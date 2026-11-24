import os

def write_notes(filename, content):
    with open(filename, "w") as file:
        file.write(content)

    print("Notes saved successfully!")
def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    else:
        return "No notes file exists yet."
while True:
    print("\n===== STUDENT NOTES MANAGEMENT =====")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        content = input("Enter your notes: ")
        write_notes("notes.txt", content)

    elif choice == "2":
        notes = read_notes("notes.txt")
        print("\nSaved Notes:")
        print(notes)

    elif choice == "3":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")