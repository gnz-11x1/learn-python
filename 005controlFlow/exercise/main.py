# example 1

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

# # example 2

name = input("Enter your name: ")

if name == "":
    print("You didn't type in your name!")
else:
    print(f"Hello {name}")

# example 3 # use of boolean with if statement

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This ite is NOT for sale")
