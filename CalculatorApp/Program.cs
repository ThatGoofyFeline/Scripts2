using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Simple Calculator");

        // Get input for the first number
        Console.Write("Enter the first number: ");
        double num1 = Convert.ToDouble(Console.ReadLine());

        // Get input for the operation
        Console.Write("Enter the operation (+, -, *, /): ");
        char operation = Console.ReadLine()[0]; // Read only the first character

        // Get input for the second number
        Console.Write("Enter the second number: ");
        double num2 = Convert.ToDouble(Console.ReadLine());

        // Perform the calculation based on the operation
        double result = 0.0;
        switch (operation)
        {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                // Check for division by zero
                if (num2 != 0)
                {
                    result = num1 / num2;
                }
                else
                {
                    Console.WriteLine("Error: Cannot divide by zero.");
                    return; // Exit the program
                }
                break;
            default:
                Console.WriteLine("Error: Invalid operation.");
                return; // Exit the program
        }

        // Display the result
        Console.WriteLine($"Result: {result}");
    }
}