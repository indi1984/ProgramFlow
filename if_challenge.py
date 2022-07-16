from numpy import kaiser


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Hello {}, welcome to the holiday.".format(name))
else:
    print("Appologies {}, you are not within age to enter.".format(name))
