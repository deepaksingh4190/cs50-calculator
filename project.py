import sys

def menu():

    print("\n Calculator\n")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

    choice = input("Select an option (1\\2\\3\\4\\5): ")

    if choice == "1":
        add()
    elif choice == "2":
        subtract()
    elif choice == "3":
        multiply()
    elif choice == "4":
        divide()
    elif choice == "5":
        sys.exit("Thank's  for using Calculator")
    else:
        sys.exit("Invalid Choice")

def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"{num1} + {num2} = {num1 + num2}")
    menu()

def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"{num1} - {num2} = {num1 - num2}")
    menu()

def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"{num1} * {num2} = {num1 * num2}")
    menu()

def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("Division by zero is invalid")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
    menu()

def main():
    menu()
if __name__ == "__main__":
    main()
