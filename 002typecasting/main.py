# typecasting = The process of converting a value of one data type to another (string, integer, float, boolean)
# Explicit vs Implicit

# Explicit Typecasting

name = "Bro"
age = 21
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# int to float
age = float(age)
print(age)
print(type(age))

# float to int
gpa = int(gpa)
print(gpa)
print(type(gpa))

# boolean to str
student = str(student)
print(student)
print(type(student))

# int to boolean
age = bool(age)
print(age) # empty or zero will only be false, otherwise everything else will be True

# Implicit Typecasting

x = 2
y = 2.0

x = x/y

print(x)