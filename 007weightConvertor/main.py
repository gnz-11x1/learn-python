# weight convertor

unit = input("Kilograms or Pounds? (K or L): ")
weight = float(input("Enter your weight: "))



if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"You weight is : {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"You weight is : {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

