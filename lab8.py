
print("----- STUDENT GRADE EVALUATION SYSTEM -----")

name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))

total = 0
failed = False

for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))

    if marks < 0 or marks > 100:
        print("Invalid Marks! Enter marks between 0 and 100.")
        exit()

    total = total + marks

    if marks < 40:
        failed = True

percentage = (total / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"

elif percentage >= 90:
    result = "PASS"
    grade = "A+"
    remark = "Outstanding"

elif percentage >= 80:
    result = "PASS"
    grade = "A"
    remark = "Excellent"

elif percentage >= 70:
    result = "PASS"
    grade = "B"
    remark = "Very Good"

elif percentage >= 60:
    result = "PASS"
    grade = "C"
    remark = "Good"

elif percentage >= 50:
    result = "PASS"
    grade = "D"
    remark = "Satisfactory"

elif percentage >= 40:
    result = "PASS"
    grade = "E"
    remark = "Pass"

else:
    result = "FAIL"
    grade = "F"
    remark = "Fail"

print("\n========== STUDENT REPORT CARD ==========")
print(f"Student Name : {name}")
print(f"Roll Number  : {roll}")
print("-----------------------------------------")
print(f"Total Marks  : {total}/500")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remark       : {remark}")
print("=========================================")
