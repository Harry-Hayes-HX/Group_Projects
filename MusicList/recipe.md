# EXAMPLE

##DESCRIPTION:
#PROGRAM WILL ASK USER WHAT SONGS THEYVE LISTENED TO RECENTLY
#TAKE INPUT FROM USER 
#ADD USER TO DICT FOR SHORT TERM STORAGE ( i couldnt be arsed) 
#USER CAN ASK TO REVIEW SONG LIST


class Music:
    # User-facing properties:
    #   input: string
    #   output: string

    def __init__(self):
        pass # No code here yet

    def Display_menu(self):
        #outputs a formatted menu code
        pass

    def Get_user_input(self):

        # Parameters: None
        # Data Types: None
        # Side Effects: 
        #   Reads user input from the console (intended to be a menu choice)
        #   May raise ValueError if the input is not a valid integer
        

    def Process_choice(self):
        #Parameters:
        #   choice: int
        # Side Effects:
        #   Calls different methods based on the user's choice
        #   May raise an AttributeError if the chosen method does not exist
        pass

    def Add_music(self, song=None, artist=None):
        # Parameters:
        #   song: string representing a single song
        #   artist: string representing a single artist
        # Returns:
        #   "added{song} to database"
        # Side-effects
        #   Saves the task to the self object dict and the text file 
        pass # No code here yet

    def List_music(self):
        # Returns:
        #   A string a list of all songs added this session or all songs added ever
        # Side-effects:
        #   Throws an exception if no songs are set
        pass # No code here yet


def main():
    pass

if __name__ == "__main__":
    main()




"""

given a menu
mock valid menu input to pick either add or list methods 
work way thru meno w mocked input


Given a song
tells the user what songs theyve listened to
"""
music = Music()
music.Add_music()
mock user input for song
assert dict is returned correctly, assert that song added to text file

"""
Given a invalid data type
music raises an exception
"""
music = Music()
music.Add_music() 
mock no user input (just press enter)
assert music == an error message then restarting the prog


call list w valid data in dict
(all methods will have defualt values that can be overwritten by providing args when calling the functions for the sake of not having to mock my menu user input every time i want to test something. for instance why mock the user ad add input to test the list method. much easier to just call the add func w provided args then call the list func)

music = Music()
music.Add_music("fwytyk", "I Prevail")
music.List_music()
check output is correct

"""
call List_music w out adding any music
music raises an exception
catch error
return error message and restart prog

music = Music()
music.List_music()
error handling
check output error message is correct