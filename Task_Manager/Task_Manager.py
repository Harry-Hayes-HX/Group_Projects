from io import StringIO
import os
import platform
import time
import sys

def clear_console(testing=False):
    if not testing:
        os.system('cls' if os.name == 'nt' else 'clear')

class TaskManager():
    #user-facing properties:
    #   int: int
    #   task: string1
    #   description: string
    #   importance: int
    #   completion: string
    #   modification: string
    #   complete: string
    #   delete: string

    def __init__(self):
        # Creates a dictionary called Tasks to store tasks and their details
        self.Tasks = {}
        self.output = StringIO()

    def display_menu(self):
        # Parameters: None
        # Data Types: None
        # Side Effects: Prints the menu options to the console
        clear_console()  # Clear previous output
        print("-----MENU-----")
        print("1: Add_tasks")
        print("2: List_tasks")
        print("3: Modify_tasks")
        print("4: Complete_tasks")
        print("5: Delete_tasks")
        print("6: QUIT")

    def get_user_choice(self):
        # Parameters: None
        # Data Types: None
        # Side Effects: Reads user input from the console (intended to be a menu choice)
        #               May raise ValueError if the input is not a valid integer
        try:
            choice = int(input("Pick a function by typing its corresponding number: "))
            return choice
        except (TypeError, ValueError):
            return None

    def process_choice(self, choice):
        # Parameters:
        #   choice (int): The user's selected option from the menu
        # Data Types:
        #   choice: integer
        # Side Effects: Calls different methods based on the user's choice
        #               May raise an AttributeError if the chosen method does not exist
        if choice == 1:
            return "add_tasks"
        elif choice == 2:
            return "picked 2"
        elif choice == 3:
            return "picked 3"
        elif choice == 4:
            return "picked 4"
        elif choice == 5:
            return "picked 5"
        elif choice == 6:
            return "picked 6"
        else:
            return "You must input a valid number. Goodbye"
        
    def Add_tasks(self):
        # Parameters:
        #   taskName (str): The name of the task to be added
        #   description (str): A short description of the task
        #   importance (int): An integer representing the value of the task upon completion
        #   completion (str): A string representing whether the task is completed or not
        # Data Types:
        #   taskName: string
        #   description: string
        #   importance: integer
        #   completion: string
        # Side Effects: Modifies the self.Tasks dictionary to add a new task with the provided details
        #               May raise a ValueError or TypeError if input is not in the expected format
        clear_console()  # Clear console before entering the loop
        while True:
            taskName = input("Enter the task name: ").strip()  # Strip newline character from the input

            if taskName in self.Tasks:
                print("The task already exists.")
                choice = input("Do you want to view the tasks? (yes or no): ").lower().strip()
                if choice == 'yes':
                    clear_console()
                    self.List_tasks()
                else:
                    break
            else:
                description = input("Enter a short description of the task: ")

                while True:
                    importance_input = input("Enter the importance (an integer value) of the task: ")
                    try:
                        importance = int(importance_input)
                        break  # Exit the loop if the input is a valid integer
                    except ValueError:
                        print("Invalid input. Please enter an integer value for importance.")

                while True:
                    completion = input("Is the task completed? (yes or no): ").lower().strip()
                    if completion in ["yes", "no"]:
                        break
                    else:
                        print("Invalid input. Please enter either 'yes' or 'no'.")

                self.Tasks[taskName] = {
                "description": description,
                "importance": importance,
                "completion": completion,
            }

            while True:
                clear_console()
                choice = input("Do you want to add another task? (yes or no): ").lower().strip()
                if choice in ["yes", "no"]:
                    break
                else:
                    sys.stdout.write("Invalid input. Please enter either 'yes' or 'no'.")  # Use sys.stdout.write() instead of print()

            if choice == "no":
                break
            clear_console()  # Clear console before restarting the loop

        # Use sys.stdout.write() to print the message and capture it in the output attribute
        sys.stdout.write("The task already exists.\n")



    def List_tasks(self, testing=False):
        # Returns:
        #   a list of tasks organized by importance (sorted based on importance in descending order)
        # Side-effects:
        #   Throws an exception if a task is not set

        # If no tasks are found, inform the user and return an empty list
        if not self.Tasks:
            print("No tasks found.")
            return []

        # Ask the user if they want to see completed tasks
        show_completed = input("Do you want to see completed tasks? (yes or no): ").lower().strip()
        while show_completed not in ["yes", "no"]:
            print("Invalid input. Please enter either 'yes' or 'no'.")
            show_completed = input("Do you want to see completed tasks? (yes or no): ").lower().strip()


        # Based on the user's choice, show all tasks or only non-completed tasks
        if show_completed == 'yes':
            # Show all tasks
            sorted_tasks = sorted(
                ((name, task) for name, task in self.Tasks.items()),
                key=lambda x: x[1]['importance'],
                reverse=True
            )
        else:
            # Show only non-completed tasks
            sorted_tasks = sorted(
                ((name, task) for name, task in self.Tasks.items() if task['completion'].lower() == 'no'),
                key=lambda x: x[1]['importance'],
                reverse=True
            )

        # Do not clear the console before printing the tasks
        # clear_console()

        # Print the header
        print("----------------------------TASK LIST-------------------------------")
        print("Task name -- Task description -- Task importance (5-1) -- Completed?")

        # Prepare the task list with importance, description, and completion (if needed)
        task_list = []
        for task_name, task_data in sorted_tasks:
            task_details = (task_name, task_data['description'], task_data['importance'])
            if show_completed == 'yes':
                task_details += (task_data['completion'],)
            task_list.append(task_details)

            # Print the task details
            print(f"{task_name} -- {task_data['description']}, {task_data['importance']} ({5 - task_data['importance'] + 1}), {task_data['completion']}")

        if testing:  # If testing is True, don't wait for input before clearing the console
            return task_list

        # Remove the wait for user input
        # input("Press Enter to continue...")
        # clear_console()
        return task_list
        
    def Modify(self, task, modification):
        # Parameters:
        #   task (str): The name of an existing task to be modified
        #   modification (str): A short description to replace the original description
        # Returns:
        #   str: A confirmation message for the modification
        # Side-effects:
        #   Modifies the description of an existing task
        #   Asks if the user wants to add the task if it doesn't exist
        if task not in self.Tasks:
            return f"Task '{task}' does not exist."

        if self.Tasks[task]['completion'].lower() == 'no':
            self.Tasks[task]['description'] = modification
            return f"Task '{task}' has been modified with the new description: '{modification}'."
        else:
            return f"You cannot edit completed task '{task}'."
        
    def Complete(self):
        while True:
            # List all non-completed tasks
            task_list = self.List_tasks(testing=True)

            if not task_list:
                print("No tasks available to mark as complete.")
                input("Press Enter to continue...")
                clear_console()
                break

            task_name = input("Enter the name of the task you want to mark as complete: ")

            if task_name not in self.Tasks:
                print("Task not found.")
                add_task = input("Do you want to add this task? (yes or no): ").lower().strip()
                if add_task == 'yes':
                    self.Add_tasks()
                    clear_console()
                    continue
                else:
                    input("Press Enter to continue...")
                    clear_console()
                    break

            task = self.Tasks[task_name]

            if task['completion'].lower() == 'yes':
                print(f"Task '{task_name}' is already marked as complete.")
                input("Press Enter to continue...")
                clear_console()
                continue

            choice = input(f"Do you want to mark '{task_name}' as complete? (yes or no): ").lower().strip()

            if choice == 'yes':
                task['completion'] = 'yes'
                print(f"Task '{task_name}' has been marked as complete.")
                input("Press Enter to continue...")
                clear_console()
                break
            elif choice == 'no':
                continue
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                input("Press Enter to continue...")
                clear_console()

def main():
    task_manager = TaskManager()
    while True:
        task_manager.display_menu()
        choice = task_manager.get_user_choice()
        if choice is None:
            print("Invalid input. Please enter a valid number.")
            time.sleep(1)
        elif choice == 1:
            task_manager.Add_tasks()
        elif choice == 2:
            # Do not clear the console before listing tasks
            # clear_console()
            task_manager.List_tasks()
            input("Press Enter to continue...")  # Wait for user input before clearing the console
            # Do not clear the console after listing tasks
            # clear_console()
        elif choice == 3:
            task_name = input("Enter the name of the task you want to modify: ")
            if task_name not in task_manager.Tasks:
                print(f"Task '{task_name}' does not exist.")
                input("Press Enter to continue...")  # Wait for user input before clearing the console
                clear_console()  # Clear console after showing the message
                continue

            if task_manager.Tasks[task_name]['completion'].lower() == 'yes':
                print(f"You cannot edit completed task '{task_name}'.")
                input("Press Enter to continue...")  # Wait for user input before clearing the console
                clear_console()  # Clear console after showing the message
                continue

            modification = input("Enter the new description for the task: ")
            result = task_manager.Modify(task_name, modification)
            print(result)
            input("Press Enter to continue...")  # Wait for user input before clearing the console
            clear_console()  # Clear console after showing the modification result
        elif choice == 4:
            task_manager.Complete()  # Call the Complete method when option 4 is selected
        elif choice == 6:
            print("Goodbye.")
            break
        else:
            result = task_manager.process_choice(choice)
            print(result)

if __name__ == "__main__":
    main()