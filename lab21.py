filename = "document.txt"
with open(filename, "w") as file:
    file.write("Python is a programming language.\n")
    file.write("It is easy to learn and use.\n")
    file.write("Python is used in AI and Machine Learning.\n")

def get_document_statistics(filename):
    with open(filename, "r") as file:
        content = file.read()

    line_count = len(content.splitlines())
    word_count = len(content.split())
    char_count = len(content)

    return line_count, word_count, char_count
def display_document(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    print("\n===== DOCUMENT CONTENT =====")

    for i, line in enumerate(lines, 1):
        print(i, ".", line.strip())
while True:
    print("\n===== DOCUMENT STATISTICS TOOL =====")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        line_count, word_count, char_count = get_document_statistics(filename)

        print("\n===== DOCUMENT STATISTICS =====")
        print("Total Lines:", line_count)
        print("Total Words:", word_count)
        print("Total Characters:", char_count)

    elif choice == "2":
        display_document(filename)

    elif choice == "3":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")