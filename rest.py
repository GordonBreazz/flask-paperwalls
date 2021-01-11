import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
papers = [
    {'id': 0,
     'title': 'title image',
     'author': 'author image',
     'path': '\..\..\',
     'tags': ['tag1', 'tag2', 'tag3']},

]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Papers wall</h1>
<p>A prototype API for papers image.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(papers)

app.run()