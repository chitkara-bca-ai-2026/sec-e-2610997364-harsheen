#Student fees calculator
#taking user input 
name=input("enter your name: ")
tutionfees=input("enter tution fees: ")
examfees=input("enter exam fees: ")
libfees=input("enter library fees: ")

#calculating semester fees before discount
total=int(tutionfees)+int(examfees)+int(libfees)

#calculating the fees after discount
discount=float(input("enter discount percentage: "))
total_discount=total*(discount/100)
total_after_discount=total-total_discount

#calculating the annual fees
annual=int(total_after_discount)*2

#calculating monthly expenses
monthly=int(total_after_discount)/6

#displaying the result
print("\n====STUDENT FEES====")
print("\nStudent name:",name)
print("------------------------")
print("Total fees:",total)
print("Annual fees:",annual)
print("Monthly expenses:",monthly)
print("=======================")