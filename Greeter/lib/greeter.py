def say_hello(name):
    try:
        return "hello " + name
    except TypeError:
        return "Error, you must call this function with a name"