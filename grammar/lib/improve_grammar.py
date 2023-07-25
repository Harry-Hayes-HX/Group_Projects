"""
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
"""


"""
Function name: grammar_check()
Arguments: str txt 
Returns:  str txt 
Tests: 

# "I am happy." -> "Correct"
# "i am happy." -> "Incorrect. The first letter needs to be capitalised."
# "I am happy" -> "Incorrect. It needs a suitable sentence-ending punctuation mark" 
"""

def grammar_check(text):

    first_character = text[0]
    last_character = text[-1]
    punctuation_marks = "!?."
    if first_character.isupper(): 
        if last_character in punctuation_marks: 
            return "Correct"
        else: 
            return "Incorrect. It needs a suitable sentence-ending punctuation mark" 
    else: 
        return "Incorrect. The first letter needs to be capitalised."


