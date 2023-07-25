def RSC(text):
    try:
        text = text
        with open(text,'r') as file:
            content = file.read()
            content = content.split()
            output = len(content)
            result = output / 200
            return "it will take " + str(result) + " minutes"
    except FileNotFoundError as e:
        return("You need to specify a valid path to a text file")

