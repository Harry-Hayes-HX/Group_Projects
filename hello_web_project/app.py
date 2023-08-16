import os
from flask import Flask, request
from flask import Flask, make_response
import sys

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"


@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"


@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"


@app.route('/submit', methods=['POST'])
def submit():
    name = request.args['name']
    message = request.args['message']

    return f"Thanks {name}, you sent this message: {message}"

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f"I am waving at {name}"

@app.route('/count_vowels', methods=["POST"])
def post_count_vowels():
    text = request.form['text']
    vowel_number = 0
    for letter in text:
        if letter in 'aeiou':
            vowel_number += 1
    return f'There are {vowel_number} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    if 'names' not in request.form:
        return "You didn't submit any names!", 400
    names = request.form['names'].split(',')
    sorted_names = sorted(names)
    return ','.join(sorted_names)

@app.route('/names', methods=['GET'])
def get_add_names():    
    if 'names' not in request.form:
        return "No names given", 400
    if " " in request.form['names']:
        return make_response("Incorrect Formatting", 400)
    name_list = ['Julia', 'Alice', 'Karim']
    names = request.form['names'].split(',')
    for name in names:
        name_list.append(name)
    sorted_names = sorted(name_list)
    return ', '.join(sorted_names)
    

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

