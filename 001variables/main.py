# Variable = A container for a value (string, integer, float, boolean)
#           A variable behaves as if it was the value it contains

# Strings
first_name = "Sayak"
food = "pizza"
email = "Bro123@fake.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
age = 25
quantity = 3
no_Of_Students = 30

print(f"You are {age} years old")
print(f"You're buying {quantity} items")
print(f"There are {no_Of_Students} students in our class")

# Float
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} km")

# Boolean
is_Student = False
for_sale = True
is_Online = False

print(f"Are you student?: {is_Student}")

if is_Student:
    print("You are a Student")
else:
    print("You are NOT a Student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT for sale")

if is_Online:
    print("You are online")
else:
    print("You are offline")