from lib.improve_grammar import *

def test_grammar_check(): 
    result = grammar_check("I want to sleep.")
    assert result == "Correct"


def test_grammar_check_with_lowercase_first_letter(): 
    result = grammar_check("i want to sleep.")
    assert result == "Incorrect. The first letter needs to be capitalised."


def test_grammar_check_without_punctuation_mark(): 
    result = grammar_check("I want to sleep")
    assert result == "Incorrect. It needs a suitable sentence-ending punctuation mark" 

