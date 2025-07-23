import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg
#python3 second.py Ajay

print("Welcome to the greeter program")
name = input("Enter your name: ")
if name == "" :
    name = sys.argv[1]
print("Greetings " + name)

print("calculator program")
firstnumber = input("Enter first number :")
secondnumber = input("Enter second number :")
print("Sum of two numbers is ", firstnumber + secondnumber)
print(int(firstnumber) + int(secondnumber))
print("Difference between two numbers is", int(firstnumber) - int(secondnumber))
print(int(firstnumber) * int(secondnumber))
print(int(firstnumber) / int(secondnumber))