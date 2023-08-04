import os
import time
import sys
import platform


def clear_console():
        #clears console when called
        os.system('cls' if os.name == 'nt' else 'clear')

class Music():



    def __init__(self):
        self.musiclist = {} 

    

    def Display_menu(self):
        clear_console()
        #Parameters: None
        #Data Types: None
        #Side Effects: prints menu options to console
        menu = "----------MENUS----------\n" \
            "1: Add music to list\n" \
            "2: List music on list\n" \
            "3: Quit\n"
        print(menu)
        return menu

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

    def Add_music(self, artists, songs):
        try:
            if artists in self.musiclist:
                if songs in self.musiclist[artists]:
                    sys.stdout.write("Song already in database, try again")
                    input("Press Enter to continue...")
                else:
                    self.musiclist[artists].append(songs)
            else:
                self.musiclist[artists] = [songs]

        except (ValueError, TypeError) as e:
            return f"An error occured, try again{e}"
        

        
    def Add_main(self):
        artist = input("Enter the artists name: ")
        songs = input("enter the name of the song: ")

        try:
            self.Add_music(artist, songs)
            sys.stdout.write("song succesfully added")

        except ValueError as e:
            return f"Error code {e} starting from menu!"
        
    def List_music(self=None):
        if self.musiclist != None:
            return self.musiclist
            input("Press Enter to continue...")
        else:
            sys.stdout.write("you need to add some music first")
            input("Press Enter to continue...")







def Main():
    build = Music()
    while True:
        build.Display_menu()
        choice = build.get_user_choice()
        if choice is None:
            sys.stdout.write("Invalid choice! please choose a valid menu option (1-3)")
            sys.stdout.write("\n")
            input("Press enter to continue... ")
        elif choice == 1:
            result = build.Add_main()
            print(result)
        elif choice == 2:
            result = build.List_music()
            print(result)
        elif choice == 3:
            sys.stdout.write("Goodbye")
            break
        else:
            sys.stdout.write("Invalid choice! please choose a valid menu option (1-3)")

            


if __name__ == "__main__":
    Main()