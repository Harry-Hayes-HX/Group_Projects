# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie


# Request:
GET /names?add=Eddie,Harry

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie, Harry



# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Alice, Eddie, Julia, Karim


# Request:
GET /names?add=

# This route should return a list of pre-defined names, plus the name given.

# Expected response (400 BAD REQUEST):
"No names given"



# Request:
GET /names?add=Eddie, Harry

# This route should return a list of pre-defined names, plus the name given.

# Expected response (400 BAD REQUEST):
"Incorrect Formatting"