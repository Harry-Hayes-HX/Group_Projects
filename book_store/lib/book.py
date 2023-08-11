class Book():

    def __init__(self, id, title, auther_name):
        self.id = id
        self.title = title
        self.auther_name = auther_name
    

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"({self.id}, {self.title}, {self.auther_name})"
