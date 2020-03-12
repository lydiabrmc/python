name = str(input("What is your name? "))
print("Welcome " + name + "!")

name = str(input("What is your name? "))
if name != "Alice":
    print("You're not Alice")

password = str(input("Please enter password "))
if password == "qwerty123":
    print("You have successfully logged in")
else:
    print("Password failure")

number = int(input("Please enter a number "))
if (number%2==0):
    print("Even")
else:
    print("Odd")

number1 = int(input("Please enter first number "))
number2 = int(input("Please enter second number "))
if (number1+number2 > 21):
    print("Bust")
else: 
    print("Safe")