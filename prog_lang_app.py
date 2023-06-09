# Import flask. Add the Flask.request object.
from flask import Flask, request
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
# @app.get('/programming_languages')
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}

# Create programming language method.
def create_programming_language(new_lang):
   language_name = new_lang['name']
   in_memory_datastore[language_name] = new_lang
   return new_lang
    
# Create a detail endpoint to retrieve a specific programming language resource from the datastore. 
# @app.route('/programming_languages/<programming_language_name>')
def get_programming_language(programming_language_name):
   return in_memory_datastore[programming_language_name]

# Update a programming language
def update_programming_language(lang_name, new_lang_attributes):
   lang_getting_update = in_memory_datastore[lang_name]
   lang_getting_update.update(new_lang_attributes)
   return lang_getting_update

# Delete a programming language
def delete_programming_language(lang_name):
   deleting_lang = in_memory_datastore[lang_name]
   del in_memory_datastore[lang_name]
   return deleting_lang

# Build a CREATE Endpoint / Post Route
@app.route('/programming_languages', methods=['GET', 'POST'])
def programming_languages_route():
   if request.method == 'GET':
       return list_programming_languages()
   elif request.method == "POST":
       return create_programming_language(request.get_json(force=True))
   
# Build an UPDATE Endpoint / Put Route
@app.route('/programming_languages/<programming_language_name>', methods=['GET', 'PUT', 'DELETE'])
def programming_language_route(programming_language_name):
   if request.method == 'GET':
      return get_programming_language(programming_language_name)
   elif request.method == "PUT":
      return update_programming_language(programming_language_name, request.get_json(force=True))
   elif request.method == "DELETE": # Build DELETE Endpoint / Delete Route
      return delete_programming_language(programming_language_name)

