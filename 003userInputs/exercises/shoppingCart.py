item = input("What item you buy?: ")
price = float(input("What's the price of the item?: "))
quantity = int(input("What's the quantity of the item?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"You bought {item} and your total bill is: ${round(total, 2)}")