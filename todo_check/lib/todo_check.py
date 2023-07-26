'''
FUNCTION NAME: tdc

PARAMETERS: userinput, text, str
OUTPUT: if true: "You have things to do
        if false: "you do not have things to do"







'''

def tdc(text):
    text = text
    with open(text, 'r') as file:
            content = file.read()
            if "#TODO" in content:
                  return "You have things to do"
            else:
                  return "you do not have things to do"


