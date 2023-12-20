class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the to-do list.')
        else:
            print(f'Task "{task}" not found in the to-do list.')

    def view_tasks(self):
        if not self.tasks:
            print('The to-do list is empty.')
        else:
            print('To-Do List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

# Main program
def main():
    todo_list = TodoList()

    while True:
        print('\n1. Add Task')
        print('2. Remove Task')
        print('3. View Tasks')
        print('4. Quit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Enter the task to remove: ')
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__ == "__main__":
    main()