
print("----- CALENDAR VERIFICATION SYSTEM -----")

year = int(input("Enter a four-digit year: "))

if year <= 0:
    print("Invalid Year! Please enter a positive year.")

elif year % 400 == 0:
    print(f"\nYear: {year}")
    print("Result: Leap Year")
    print("Reason: Century year divisible by 400")
    print("Days in February: 29")
    print("Total days in year: 366")

elif year % 100 == 0:
    print(f"\nYear: {year}")
    print("Result: Common Year")
    print("Reason: Century year not divisible by 400")
    print("Days in February: 28")
    print("Total days in year: 365")

elif year % 4 == 0:
    print(f"\nYear: {year}")
    print("Result: Leap Year")
    print("Reason: Divisible by 4 and not a century year")
    print("Days in February: 29")
    print("Total days in year: 366")

else:
    print(f"\nYear: {year}")
    print("Result: Common Year")
    print("Reason: Not divisible by 4")
    print("Days in February: 28")
    print("Total days in year: 365")
