class Task_Manager():
    #user-facing properties:
    #   int: int
    #   task: string
    #   description: string
    #   importance: int
    #   completion: string
    #   modification: string
    #   complete: string
    #   delete: string

    def __init__(self):
        #creates a dictionary called Tasks
        self.Menu()
        pass #skip

    def Menu(self, int):
        #Parameters:
        #   name: int
        #Side effects:
        '''   set the int porperty of the self object to pick what to do 
              next (ie add a task, review a task, mark a task as complete or delete a task)
    
    def Add_tasks(self, task, description, importance, completion="completed"):
        # Parameters:
        #   task: string representing a single task
        #   description: string representing a short description of the
        #   task
        #   importance: int representing the value of a task upon
        #   completion
        #   completion: string representing wether a task is completed or not.
        #   defualt value is "completed"
        # Returns:
        #   confirmation that task has been added
        # Side-effects:
        #   adds the task to self object dictionary
        pass # skip

    def List_tasks(self):
        # Returns:
        #   a list of tasks orginised by importance(number)
        # Side-effects:
        #   Throws an exception if a task is not set
        pass #skip

    def Modify(self, task, modification):
        # Parameters:
        #   task: string representing the name of an existing task
        #   modification: string representing a short description of a
        #   task to replace the original description
        # Returns:
        #   confirmation of modification
        # Side-effects:
        #   throws an exception if a task doesnt exist - asks if you want to add the
        #   task
    
    def Complete(self, complete):
        # Parameters:
        #   complete: string representing the status of the task, replaces string that
        #   refers to if the task is done or not
        # Returns:
        #   confirmation of task completion being marked
        #   returns an error if task doesnt exist and start flow over

    def Delete(self, delete):
        # Parameters:
        #   delete: strint representing the name of an existing task
        # Returns:
        #   confirmation that task key and values have been deleted
        # Side-effects:
        #   returns an error if task doesnt exist or if something goes wrong when
        #   deleting a task





        # def Menu(self, choice=None):
    #     
    #         print("-----MENU-----")
    #         print("1: Add_tasks")
    #         print("2: List_tasks")
    #         print("3: Modify_tasks")
    #         print("4: Complete_tasks")
    #         print("5: Delete_tasks")
    #         print("6: QUIT")
            
    #     try:
    #         if choice is None:
    #             choice = int(input("Pick a function by typing its corresponding number: "))
    #             print(choice)
    #             if choice == 1:
    #                 self.Add_tasks()
    #                 return "picked 1"
    #             elif choice == 2:
    #                 return "picked 2"
    #             elif choice == 3:
    #                 return "picked 3"
    #             elif choice == 4:
    #                 return "picked 4"
    #             elif choice == 5:
    #                 return "picked 5"
    #             elif choice == 6:
    #                 return "picked 6"
    #             else:
    #                 return "You must input a valid number. Goodbye"
            
    #     except (TypeError, ValueError) as e:
    #         return "an error has occured"



    
        # Parameters:
        #   task: string representing a single task
        #   description: string representing a short description of the
        #   task
        #   importance: int representing the value of a task upon
        #   completion
        #   completion: string representing wether a task is completed or not.
        #   defualt value is "completed"
        # Returns:
        #   confirmation that task has been added
        # Side-effects:
        #   adds the task to self object dictionary
        # Tasks = self.Tasks

        # try:
        #     taskName = str(input("Enter a Task name: "))
        #     description = str(input("Enter a short description of the task: "))
        #     importance = int(input("enter a number from 1 to 5, 5 being the most important task, 1 being the least: "))

        #     if Tasks.get(taskName) is not None:
        #         Tasks[taskName] = [description, importance]
        #         print(Tasks)
        #     else:
        #         return "that task already exists"
        # except (ValueError, TypeError) as e:
        #     return "error, you need to input a valid task name, description and importance value."
        
    

    # def List_tasks(self):
    #     # Returns:
    #     #   a list of tasks orginised by importance(number)
    #     # Side-effects:
    #     #   Throws an exception if a task is not set
    #     pass #skip

    # def Modify_tasks(self, task, modification):
    #     # Parameters:
    #     #   task: string representing the name of an existing task
    #     #   modification: string representing a short description of a
    #     #   task to replace the original description
    #     # Returns:
    #     #   confirmation of modification
    #     # Side-effects:
    #     #   throws an exception if a task doesnt exist - asks if you want to add the
    #     #   task
    #     pass #skip
    
    # def Complete_tasks(self, complete):
    #     # Parameters:
    #     #   complete: string representing the status of the task, replaces string that
    #     #   refers to if the task is done or not
    #     # Returns:
    #     #   confirmation of task completion being marked
    #     #   returns an error if task doesnt exist and start flow over
    #     pass #skip

    # def Delete_tasks(self, delete):
    #     # Parameters:
    #     #   delete: strint representing the name of an existing task
    #     # Returns:
    #     #   confirmation that task key and values have been deleted
    #     # Side-effects:
    #     #   returns an error if task doesnt exist or if something goes wrong when
    #     #   deleting a task
    #     pass #skip

