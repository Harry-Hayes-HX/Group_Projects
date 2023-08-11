from lib.book import *

def test_book_constructs():
    build = Book(1, "book1", "Harry")
    assert build.id == 1
    assert build.title == "book1"
    assert build.auther_name == "Harry"

def test_books_formatting():
    build = Book(1, "book1", "Harry")
    assert str(build) == "(1, book1, Harry)"

def test_artists_are_equal():
    build1 = Book(1, "book1", "Harry")
    build2 = Book(1, "book1", "Harry")
    assert build1 == build2