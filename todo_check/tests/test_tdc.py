from lib.todo_check import *

def test():
    build = tdc("lib/text1.txt")
    assert build == "You have things to do"
    build = tdc("lib/text2.txt")
    assert build == "you do not have things to do"

