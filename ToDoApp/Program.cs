using System;
using System.Collections.Generic;

class TodoList
{
    private List<string> tasks;

    public TodoList()
    {
        tasks = new List<string>();
    }

    public void AddTask(string task)
    {
        tasks.Add(task);
        Console.WriteLine($"Task \"{task}\" added to the to-do list.");
    }

    public void RemoveTask(string task)
    {
        if (tasks.Contains(task))
        {
            tasks.Remove(task);
            Console.WriteLine($"Task \"{task}\" removed from the to-do list.");
        }
        else
        {
            Console.WriteLine($"Task \"{task}\" not found in the to-do list.");
        }
    }

    public void ViewTasks()
    {
        if (tasks.Count == 0)
        {
            Console.WriteLine("The to-do list is empty.");
        }
        else
        {
            Console.WriteLine("To-Do List:");
            for (int i = 0; i < tasks.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {tasks[i]}");
            }
        }
    }
}

class Program
{
    static void Main()
    {
        TodoList todoList = new TodoList();

        while (true)
        {
            Console.WriteLine("\n1. Add Task");
            Console.WriteLine("2. Remove Task");
            Console.WriteLine("3. View Tasks");
            Console.WriteLine("4. Quit");

            Console.Write("Enter your choice (1-4): ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Console.Write("Enter the task: ");
                    string taskToAdd = Console.ReadLine();
                    todoList.AddTask(taskToAdd);
                    break;

                case "2":
                    Console.Write("Enter the task to remove: ");
                    string taskToRemove = Console.ReadLine();
                    todoList.RemoveTask(taskToRemove);
                    break;

                case "3":
                    todoList.ViewTasks();
                    break;

                case "4":
                    Console.WriteLine("Goodbye!");
                    return;

                default:
                    Console.WriteLine("Invalid choice. Please enter a number between 1 and 4.");
                    break;
            }
        }
    }
}