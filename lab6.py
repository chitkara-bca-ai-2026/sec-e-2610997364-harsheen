
print("----- CLOTHING STORE BILLING SYSTEM -----")

customer = input("Enter Customer Name: ")
garment = input("Enter Garment Name: ")
price = float(input("Enter Price per Garment: "))
quantity = int(input("Enter Quantity: "))

total = price * quantity

print("\n========== CUSTOMER BILL ==========")
print(f"Customer Name: {customer}")
print(f"Garment Name: {garment}")
print(f"Price per Unit: Rs. {price}")
print(f"Quantity: {quantity}")
print(f"Total Amount: Rs. {total}")

print("===================================")
