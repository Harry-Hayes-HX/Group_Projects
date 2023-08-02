class DiaryEntry:
    call_count = 0

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        formatted = self.title + ": " + self.contents
        return formatted
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        entry = self.title + " " + self.contents
        words = entry.split() # Split the text into a list of words
        # print(words)
        num_words = len(words)  # Get the count of words in the list
        # print(num_words)
        return num_words


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.

        word_count = self.count_words()
        output = word_count / wpm
        return output


    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.

        word_count = self.count_words() #call other function to get number of words entry including title
        # print(word_count)
        period = wpm * minutes #int that represents how many words a user can read in 1 chunk
        stop_index = period #int that represents the endpoint for slice on entry
        # print(period)
        # print(DiaryEntry.call_count)

        if DiaryEntry.call_count < 1: #checks if function has been run. if not then it moves on to the second if statement
            if word_count < period: #checks if the amount of words in the entry exceeds the mount of readable words in the given time. if theres less words in the entry than words in the period variable, it means the user can read it all in one chunk
                # print("test 2")
                output = self.title + " " + self.contents #create a variable with the title and content formatted
                # print(output)
                DiaryEntry.call_count +=1 #increase the call count to keep a record of times ran
                return output #output the formatted diary entry
            elif word_count > period: #if the word count is larger than the period this means there is more words than the user can read in one chunk
                # print("test 3")
                start_index = 0 #sets the slice notation to read from the first word
                slice_obj = slice(start_index, stop_index) #creates a slice onbject to use on the list created when splitting the text into individual words
                preformat = self.title + " " + self.contents #formats the title and content into one variable
                format = preformat.split() #assigns the entry (format) variable into a list
                formated = format[slice_obj] #uses slice on the list that reads from word 0 (first word) and continues for however many words period is (period is the wpm * the time alloted, so period is essentially the amount of words in the chunk. in this example that is 10)
                formated = ' '.join(formated) #reformats the new chunk into readable text
                DiaryEntry.call_count += 1 #increments call count for the next go around
                # print(DiaryEntry.call_count)
                # print(formated)
                return formated #returns the chunk
        elif DiaryEntry.call_count >= 1: #checks if the count of times run is more than or equal to 1 (indicating its already been run once)
            # print("test elif")
            start_index = period * DiaryEntry.call_count #create a new start index, instead of starting from 0 we want to start from the last place left of so we take the period (sum of wpm*alloted time) and times it by the count, which gives us the word just after the las word from the previous chunk. in this example that would be 5*1 start at word 5 (actually word 6) then the third time the function is run: 5*2=10 so start at word 10 (actually 11)
            stop_index = start_index + period #we now need to end on the correct word so we take the previous start_index (in this examples 2nd run that would be 5, 3rd run 10 4th 15) and add the period, which is a variable that states how many words can be in a chunk(5+5=10+5=15+5=20)
            slice_obj = slice(start_index, stop_index) #repeat of the original steps when the word count is higher than the chunk count
            preformat = self.title + " " + self.contents
            format = preformat.split()
            formated = format[slice_obj]
            formated = ' '.join(formated)
            DiaryEntry.call_count += 1 #increment 1 more time
            return formated





build = DiaryEntry("Lorem ipsum dolor sit amet,", "consectetur adipiscing elit. Duis in pharetra tortor, vitae luctus ex. Ut imperdiet urna sit amet.")
build.reading_chunk(5, 1)
build.reading_chunk(5, 1)
build.reading_chunk(5, 1)
build.reading_chunk(5, 1)