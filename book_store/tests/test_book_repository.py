from lib.book_repository import *
from lib.book import *


def test_book_repo(db_connection):
    db_connection.seed("seeds/book_store.sql")
    build = BookRepository(db_connection)
    output = build.all()
    
    assert output == [Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
    Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
    Book(3, 'Emma', 'Jane Austen'),
    Book(4, 'Dracula', 'Bram Stoker'),
    Book(5, 'The Age of Innocence', 'Edith Wharton')]