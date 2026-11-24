def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
while True:
    print("\n===== MATHEMATICS LEARNING TOOL =====")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("Enter a non-negative number: "))

        if n < 0:
            print("Please enter a non-negative number.")
        else:
            result = factorial(n)
            print("Factorial of", n, "is:", result)

    elif choice == "2":
        terms = int(input("Enter number of terms: "))

        if terms < 0:
            print("Please enter a non-negative number.")
        else:
            series = []

            for i in range(terms):
                series.append(fibonacci(i))

            print("Fibonacci Series:", series)

    elif choice == "3":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")