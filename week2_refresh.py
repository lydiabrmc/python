name = str(input("What is your name? "))
if name == "Bob":
    print("Welcome Bob!")
else:
    print("You're not Bob")
    
name = str(input("What is your name? "))
if name != "Alice":
    print("You're not Alice!")

password = str(input("Please enter password: "))
if password == "qwerty123":
    print("You have successfully logged in ")
else:
    print("Password failure")

number = int(input("Please enter a number "))
if (number%2==0):
    print("Even")
else:
    print("Odd")

num1 = int(input("Please enter first number "))
num2 = int(input("Please enter second number "))
if (num1+num2>21):
    print("Bust")
else:
    print("Safe")