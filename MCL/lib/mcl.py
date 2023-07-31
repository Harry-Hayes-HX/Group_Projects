def get_most_common_letter(text):
    counter = {}
    for char in text:
        # print(char)
        if char != ' ':
            counter[char] = counter.get(char, 0) + 1
            # print(counter)
            # print(f"sorted '{counter.items()}'") 
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    letter = letter[0][0]
    print(letter)
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")