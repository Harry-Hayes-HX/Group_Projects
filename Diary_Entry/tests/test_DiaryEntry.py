from ..lib.DiaryEntry import *

#when supplied with a title and entry
# Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
def test_format_func():
    build = DiaryEntry("Entry one", "Hello World!")
    result = build.format() 
    assert result == "Entry one: Hello World!"

def test_count_words_func():
    build = DiaryEntry("Entry one", "Hello World!")
    result = build.count_words() 
    assert result == 4

def test_reading_time():
    build = DiaryEntry("Entry one", "Hello World some more words!")
    result = build.reading_time(40)
    assert result ==  0.175

def test_reading_chunk():
    build = DiaryEntry("Entry one", "Hello World some more words!")
    result = build.reading_chunk(40, 1)
    assert result == "Entry one Hello World some more words!"
    
