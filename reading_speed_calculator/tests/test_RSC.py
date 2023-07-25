from lib.reading_speed_calc import *

def test_valid_filepath():
    build = RSC("lib/text1.txt")
    assert build == "it will take 0.125 minutes"
    build = RSC("lib/text2.txt")
    assert build == "it will take 0.5 minutes"
    build = RSC("lib/text3.txt")
    assert build == "it will take 1.0 minutes"
    build = RSC("lib/text4.txt")
    assert build == "it will take 1.5 minutes"
    build = RSC("lib/text5.txt")
    assert build == "it will take 2.0 minutes"


def test_invalid_filepath():
    build = RSC("guygu")
    assert build == "You need to specify a valid path to a text file"


