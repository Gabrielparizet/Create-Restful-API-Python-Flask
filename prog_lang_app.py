# Import flask.
from flask import Flask
# Instantiate flask app and assign it to app variable.
app = Flask(__name__)

# In memory data-store for our app (Python dictionnary)
in_memory_datastore = {
   "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
   "BASIC": {"name": "BASIC", "publication_year": 1964, "contribution": "runtime interpretation, office tooling"},
   "PL": {"name": "PL", "publication_year": 1966, "contribution": "constants, function overloading, pointers"},
   "SIMULA67": {"name": "SIMULA67", "publication_year": 1967,
                "contribution": "class/object split, subclassing, protected attributes"},
   "Pascal": {"name": "Pascal", "publication_year": 1970,
              "contribution": "modern unary, binary, and assignment operator syntax expectations"},
   "CLU": {"name": "CLU", "publication_year": 1975,
           "contribution": "iterators, abstract data types, generics, checked exceptions"},
}

# Create the list endpoint. Below the in-memory datastore dictionary, a rudimentary list endpoint fetches all the programming language resources and displays them as JSON.
@app.get('/programming_languages')
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}
    
# Create a detail endpoint to retrieve a specific programming language resource from the datastore. 
@app.route('/programming_languages/<programming_language_name>')
def get_programming_language(programming_language_name):
   return in_memory_datastore[programming_language_name]
    