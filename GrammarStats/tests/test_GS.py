from ..lib.GS import *

def test_check():
    #test check function with valid data
    build = GrammarStats()
    result = build.check("Hello World!")
    assert result == True
    result = build.check("hello World!")
    assert result == False
    result = build.check("Hello World")
    assert result == False
    


def test_PG():
    #check PG function with valid data
    build = GrammarStats()

    # Perform some checks
    build.check("Hello World!")
    build.check("hello World!")
    build.check("Hello World")
    build.check("hello world")

    # Calculate and print the percentage of good checks
    result = build.percentage_good()
    assert result == "Percentage of good checks: 25.00%"

def test_check_invalidinputs():
    #test check function with invalid inputs
    build = GrammarStats()

    # Perform some checks
    build.check("")
    build.check(7)
    build.check(False)
    build.check(None)
    build.check()

def test_PG_invalidinputs():
    #test PG function with invalid inputs
    build = GrammarStats()

    # Perform some checks
    result = build.percentage_good()
    build.check("")
    build.check(7)
    build.check(False)
    build.check(None)
    build.check()
    result = build.percentage_good(1)