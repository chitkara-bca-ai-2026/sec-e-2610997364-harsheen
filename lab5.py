
import math

print("----- ENGINEERING CALCULATION UTILITY -----")

num = float(input("Enter a number: "))
exponent = int(input("Enter exponent: "))

power = pow(num, exponent)
square_root = math.sqrt(num)

measurement = float(input("Enter decimal measurement: "))

upper = math.ceil(measurement)
lower = math.floor(measurement)

print("\n----- CALCULATION RESULTS -----")
print(f"Power: {power}")
print(f"Square Root: {square_root}")
print(f"Ceiling Value: {upper}")
print(f"Floor Value: {lower}")
