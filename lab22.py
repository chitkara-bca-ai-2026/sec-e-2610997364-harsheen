filename = "report.txt"
with open(filename, "w") as file:
    file.write("Our company achieved good sales this year.\n")
    file.write("Customer satisfaction is our main priority.\n")
    file.write("Sales increased by 20 percent this year.\n")
    file.write("Our company plans to expand its business.\n")
    file.write("Customer feedback helps improve our services.\n")

def search_keyword(filename, keyword):
    total = 0

    with open(filename, "r") as file:
        for line_no, line in enumerate(file, 1):

            if keyword.lower() in line.lower():
                count = line.lower().count(keyword.lower())
                total += count

                print("Line", line_no, ":", line.strip())
                print("Occurrences:", count)

    print("Total occurrences found:", total)

def display_document(filename):
    with open(filename, "r") as file:
        print("\n===== FULL DOCUMENT =====")
        print(file.read())
        
while True:
    print("\n===== KEYWORD SEARCH UTILITY =====")
    print("1. Search Keyword")
    print("2. View Full Document")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        keyword = input("Enter keyword to search: ")

        if keyword == "":
            print("Please enter a valid keyword.")
        else:
            search_keyword(filename, keyword)

    elif choice == "2":
        display_document(filename)

    elif choice == "3":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")