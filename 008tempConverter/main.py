
unit = input("Is this temperature is Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Celsius is: {temp}°Fahrenheit")
elif unit == "F":
    temp = round((5 * (temp - 32)/9), 1)
    print(f"The temperature in Fahrenheit is: {temp}°Celsius")
elif unit == "":
    print("Please insert a unit between C or F")
else:
    print(f"{unit} is an invalid unit of measurement")