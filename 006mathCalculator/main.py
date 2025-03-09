# Python calculator

operator = input("Choose the operator (+,-,*,/): ")
a = float(input("Choose the 1st number: "))
b = float(input("Choose the 2nd number: "))

if operator == "+":
    c = a + b
    print(f"The sum of a and b is {c}")
elif operator == "-" :
    c = a - b
    print(f"The subtraction of a and b is {c}")
elif operator == "*" :
    c = a * b
    print(f"The multiplication of a and b is {c}")
elif operator == "/" :
    c = a / b
    print(f"The division between a and b is {c}")
else :
    print("Choose the operator between +, -, *, /")