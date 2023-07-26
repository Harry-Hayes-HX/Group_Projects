from lib.greeter import *

def test():
    build = say_hello("Kay")
    assert build == "hello Kay"
    build = say_hello()
    assert build == "Error, you must call this function with a name"
    build = say_hello(6)
    assert build == "Error, you must call this function with a name"
