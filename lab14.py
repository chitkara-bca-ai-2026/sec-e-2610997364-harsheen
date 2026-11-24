
print("===== LIBRARY BOOK COLLECTION SYSTEM =====")

books = [
    ("Python Basics", "John Smith", "2020", "Programming"),
    ("Artificial Intelligence", "David", "2022", "AI"),
    ("Cloud Computing", "James", "2021", "Cloud Computing"),
    ("Robotics Guide", "Robert", "2019", "Robotics")
]

Library_categories = set()

for book in books:
    Library_categories.add(book[3])

requested_genres = {
    "AI", "Cloud Computing", "Robotics", "Cybersecurity"
}

while True:

    print("\n----- LIBRARY MENU -----")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("\n----- BOOK CATALOG -----")

        for title, author, year, category in books:
            print("Title:", title)
            print("Author:", author)
            print("Year:", year)
            print("Category:", category)
            print("----------------------")

    elif choice == 2:
        print("\nEnter New Book Details")

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        year = input("Enter Publication Year: ")
        category = input("Enter Category: ")

        new_book = (title, author, year, category)

        books.append(new_book)
        Library_categories.add(category)

        print("Book added successfully!")

    elif choice == 3:
        print("\n----- LIBRARY CATEGORIES -----")

        for category in Library_categories:
            print(category)

    elif choice == 4:
        genre = input("Enter genre for student wishlist: ")

        requested_genres.add(genre)

        print("Genre added to wishlist successfully!")

    elif choice == 5:
        print("\n----- CATEGORY GAP ANALYSIS -----")

        print("Common Categories:")
        print(Library_categories.intersection(requested_genres))

        print("\nRequested but Not Available:")
        print(requested_genres.difference(Library_categories))

        print("\nAll Categories:")
        print(Library_categories.union(requested_genres))

    elif choice == 6:
        print("Thank you! Exiting Library System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
