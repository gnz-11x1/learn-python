# if = Do some code only IF some condition is True
#       Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are two old to signed up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to signed up!")