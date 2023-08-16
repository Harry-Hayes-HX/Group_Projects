from flask import Flask, make_response

# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

def test_post_sort_names_with_a_list_of_names(web_client):
    response = web_client.post("/sort-names", data = {
        'names' : 'Joe,Alice,Zoe,Julia,Kieran'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

def test_post_sort_names_with_a_list_of_names_with_letters_at_the_end(web_client):
    response = web_client.post("/sort-names", data = {
        'names' : 'Aaaaa,Aaaaz,Aaaab'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Aaaaa,Aaaab,Aaaaz'

def test_post_sort_names_with_no_list_of_names(web_client):
    response = web_client.post("/sort-names")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "You didn't submit any names!"


def test_get_add_valid_single_name(web_client):
    response = web_client.get("/names", data = {'names' : 'Eddie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'

def test_get_add_valid_multi_name(web_client):
    response = web_client.get("/names", data = {
        'names' : 'Eddie,Harry'
        })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Harry, Julia, Karim'

def test_get_add_no_name(web_client):
    response = web_client.get("/names")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "No names given"

def test_get_add_invalid_multi_name(web_client):
    response = web_client.get("/names", data = {
        'names' : 'Eddie, Harry'
        })
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Incorrect Formatting"