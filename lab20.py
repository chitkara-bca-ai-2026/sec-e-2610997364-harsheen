filename = "daily_log.txt"

with open(filename, "w") as file:
    file.write("Office opened at 9 AM.\n")
    file.write("Team meeting completed at 11 AM.\n")
    file.write("Reports submitted successfully.\n")

def append_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")

    print("Log entry added successfully!")
def display_log(filename):
    with open(filename, "r") as file:
        entries = file.readlines()

    print("\n===== COMPLETE DAILY LOG =====")
    print("Total Entries:", len(entries))

    for i, entry in enumerate(entries, 1):
        print(i, ".", entry.strip())
while True:
    print("\n===== DAILY LOG BOOK =====")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        entry = input("Enter log entry: ")
        append_entry(filename, entry)

    elif choice == "2":
        display_log(filename)

    elif choice == "3":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")