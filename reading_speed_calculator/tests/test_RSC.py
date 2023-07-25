from lib.reading_speed_calc import *

def test_valid_filepath():
    build = RSC("lib/text.txt")
    assert build == "it will take 0.0 minutes"

def test_invalid_filepath():
    build = RSC("guygu")
    assert build == "You need to specify a valid path to a text file"


