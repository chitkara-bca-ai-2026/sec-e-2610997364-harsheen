
print("----- DATA CONVERSION UTILITY -----")

product = input("Enter Product Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

total_price = price * quantity

total_str = str(total_price)

print("\n----- TYPE CASTING SUMMARY -----")
print("Product:", type(product))
print("Price:", type(price))
print("Quantity:", type(quantity))
print("Total Price:", type(total_price))
print("Invoice Amount:", type(total_str))

print("\n========== TAX INVOICE ==========")
print(f"Product Name: {product}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total Amount: {total_str}")
