# Normal Python Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Cannot divide by 0")
        return None

def main():
    print("Welcome to the Python Calculator!")

    while True:
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        operation = input()

        if operation == '5':
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '1':
            result = add(num1, num2)
        elif operation == '2':
            result = subtract(num1, num2)
        elif operation == '3':
            result = multiply(num1, num2)
        elif operation == '4':
            result = divide(num1, num2)
        else:
            print("Invalid input!")
            continue

        print("Result:", result)

if __name__ == "__main__":
    main()