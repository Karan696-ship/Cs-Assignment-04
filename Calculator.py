print("=== Welcome to My Simple Calculator ===")

# taking values from user
a = float(input("Please enter the first number: "))
b = float(input("Please enter the second number: "))

print("\nWhat do you want to do?")
print(" +  for Addition")
print(" -  for Subtraction")
print(" *  for Multiplication")
print(" /  for Division")

op = input("Enter your choice: ")

# doing operations in clean way
if op == "+":
    print("Answer =", a + b)

elif op == "-":
    print("Answer =", a - b)

elif op == "*":
    print("Answer =", a * b)

elif op == "/":
    if b == 0:
        print("Sorry, division by zero is not possible!")
    else:
        print("Answer =", a / b)

else:
    print("Invalid option! Please choose +, -, * or /")

print("=== Thanks for using my calculator :) ===")
