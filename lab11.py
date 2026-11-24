
print("----- ACCOUNT REGISTRATION SYSTEM -----")

username = input("Enter Username: ")
password = input("Enter Password: ")


length_check = len(password) >= 8

digit_check = False
upper_check = False

for ch in password:
    if ch.isdigit():
        digit_check = True

    if ch.isupper():
        upper_check = True

print("\n----- PASSWORD VALIDATION RESULTS -----")

if length_check:
    print("[PASS] Password contains at least 8 characters")
else:
    print("[FAIL] Password must contain at least 8 characters")

if digit_check:
    print("[PASS] Password contains at least one digit")
else:
    print("[FAIL] Password must contain at least one digit")

if upper_check:
    print("[PASS] Password contains at least one uppercase letter")
else:
    print("[FAIL] Password must contain at least one uppercase letter")

if length_check and digit_check and upper_check:
    print("\nPassword is VALID")
    print(f"Account created successfully for {username}!")
else:
    print("\nPassword is INVALID")
