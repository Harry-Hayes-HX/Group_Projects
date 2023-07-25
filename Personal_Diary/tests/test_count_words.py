from lib.count_words import *

def test():
    build = count_words("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque condimentum rutrum en")
    assert build == 12
