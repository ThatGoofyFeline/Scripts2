# Geode calculator!

fun add(a, b):
    return a + b

fun sub(a, b):
    return a - b

fun mult(a, b):
    return a * b

fun div(a, b):
    if b != 0:
        return a / b
    else:
        print("Cannot divide by 0!")
        return (Null)

while True:

    # Get the user's choice
    int choice = input(/:
        print("Enter operation")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication)
        print("4: Division")
    /)

    # Get the user's numbers
    float num1 = input("Enter first number: ")
    float num2 = input("Enter second number: ")

    # Check the operation, and call the right one
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = sub(num1, num2)
    elif choice == 3:
        result = mult(num1, num2)
    elif choice == 4:
        result = div(num1, num2)
    else:
        print("Invalid input!")
        continue
    
    if Result != "(Null)":
        print("Result: " + result)