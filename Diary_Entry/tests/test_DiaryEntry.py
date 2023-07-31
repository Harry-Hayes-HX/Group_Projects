from ..lib.DiaryEntry import *

def test_func():
    build = DiaryEntry("Entry one", "Hello World!")
    assert build.format == "Entry one: Hello World!"
    
