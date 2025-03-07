def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Bug: Missing check for division by zero
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice (1/2/3/4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"Result: {add(num1, num2)}")
    elif choice == 2:
        print(f"Result: {subtract(num1, num2)}")
    elif choice == 3:
        print(f"Result: {multiply(num1, num2)}")
    elif choice == 4:
        print(f"Result: {divide(num1, num2)}")  # Bug here if num2 is 0
    else:
        print("Invalid choice!")
