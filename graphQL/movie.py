from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify

import resolvers as r

PORT = 5000
HOST = 'localhost'
app = Flask(__name__)

# todo create elements for Ariadne

# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)