def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    return base ** exp

def number(n):
    if n == int(n):
        return int(n)
    return n

history = []

while True:

    print("\n===== UTILITY CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. View History")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '8':
        print("Thank you for using calculator!")
        break

    elif choice == '7':
        print("\nCalculation History:")
        for item in history:
            print(item)

    elif choice in ['1', '2', '3', '4', '5', '6']:

        try:
            a = float(input("Enter first number: "))

            if choice == '6':
                exp = input("Enter exponent (Press Enter for default): ")

                if exp == "":
                    result = power(a)
                    record = f"{a} ** 2 = {result}"
                else:
                    b = float(exp)
                    result = power(a, b)
                    record = f"{a} ** {b} = {result}"

            else:
                b = float(input("Enter second number: "))

                if choice == '1':
                    result = add(a, b)
                    record = f"{a} + {b} = {result}"

                elif choice == '2':
                    result = subtract(a, b)
                    record = f"{a} - {b} = {result}"

                elif choice == '3':
                    result = multiply(a, b)
                    record = f"{a} * {b} = {result}"

                elif choice == '4':
                    result = divide(a, b)
                    record = f"{a} / {b} = {result}"

                elif choice == '5':
                    result = modulus(a, b)
                    record = f"{a} % {b} = {result}"

            if result is None:
                print("Error! Cannot divide by zero.")
            else:
                result = number(result)
                print("Result:", result)
                history.append(record)

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    else:
        print("Invalid choice! Please select 1 to 8.")