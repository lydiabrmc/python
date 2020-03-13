name = str(input("What is your name? "))
if name == "Alice":
    print("Hello, Alice")
elif name == "Bob":
    print("You're not Bob, I'm Bob")
else: 
    print("You must be Charlie")

age = int(input("What is your age? "))
if age < 11 and age != 0:
    print("You're too young to go to this school.")
elif age >= 11 and age <= 16:
    print("You can can come to this school.")
elif age > 16:
    print("You're too old for this school.")
else:
    print("You're not born yet!")

month = str(input("Please enter a month: "))
if month == "March" or month == "April" or month == "May":
    print(month + " is in Spring")
elif month == "June" or month == "July" or month == "August":
    print(month + " is in Summer")
elif month == "September" or month == "October" or month == "November":
    print(month + " is in Autumn")
elif month == "December" or month == "January" or month == "February":
    print(month + " is in Winter")
else: 
    print("I don't know")

num1 = int(input("Please give your first number "))
num2 = int(input("Please give your second number "))
if num1%2==0 and num2%2==0:
    print("Even")
elif num1%2!=0 and num2%2!=0:
    print("Odd")
else:
   print(num1+num2)