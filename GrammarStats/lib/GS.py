class GrammarStats:
    
    
    def __init__(self):
        self.nb_checked = 0
        self.GG = 0
  
    def check(self, text=None):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        try:
            punc = ".!?"
            first_letter = text[0]
            last_letter = text[-1]
            if first_letter.isupper() == True:
                # print("caps good")
                if last_letter in punc:
                    print("caps and punc good")
                    print("nb checked and gg incremented")
                    self.nb_checked += 1
                    self.GG += 1
                    return True
                else:
                    print("punc bad")
                    print("nb checked incremented")
                    self.nb_checked += 1
                    return False
            else:
                print("caps bad")
                print("nb checked incremented")
                self.nb_checked += 1
                return False
        except (TypeError, ValueError, IndexError) as e:
            print(f"You need to enter a valid string. ERROR CODE: {e}")
  
    def percentage_good(self, *args):
        if len(args):
            print('Too many args given! run GrammarStats.percentage_good() to see the percentage of good grammar')
        try:
            print(self.GG)
            print(self.nb_checked)
            percentage= (self.GG / self.nb_checked) * 100
            print(percentage)
            return f"Percentage of good checks: {percentage:.2f}%"
        except (ZeroDivisionError, TypeError) as e:
            print(f"something went wrong! ERROR CODE: {e}")
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
 

build = GrammarStats()
build.check(7)