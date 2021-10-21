from flask import Flask, make_response, jsonify, render_template, request
import json

app = Flask(__name__)

with open('{}/databases/movies.json'.format("."), "r") as jsf:
  movies = json.load(jsf)["movies"]

#Renvoie la page d'accueil du service
@app.route('/', methods=['GET'])
def index():
  return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)

#Renvoie un JSON contenant les livres
@app.route('/movies', methods=['GET'])
def json():
  return make_response(jsonify(movies),200)

#Renvoie un film en fonction de son id
@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
  for movie in movies:
    if str(movie["id"]) == str(movieid):
      #avec ou sans le http://127.0.0.1:5000???
      movie["links"] = {"GET": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},
                        "PUT": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},
                        "POST": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},
                        "DELETE": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]}}
      res = make_response(jsonify(movie),200)
      return res
  return make_response(jsonify({"error":"Movie ID not found"}),400)

#http://127.0.0.1:5000/moviesbytitle?title=Spectre
#Renvoie un film en fonction de son titre
@app.route("/movietitle/<title>", methods=['GET'])
def get_movie_bytitle(title):
  for movie in movies:
    if str(movie["title"]) == str(title):
      # avec ou sans le http://127.0.0.1:5000???
      movie["links"] = {"GET": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},
                        "GET": {"href": "http://127.0.0.1:5000/movietitle/" + movie["title"]},
                        "PUT": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},
                        "POST": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},
                        "DELETE": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]}}
      res = make_response(jsonify(movie), 200)
      return res
  return make_response(jsonify({"error": "Movie title not found"}), 400)

#Crée un nouveau film
@app.route("/movies/<movieid>", methods=["POST"])
def create_movie(movieid):
  req = request.get_json()
  for movie in movies:
    if str(movie["id"]) == str(movieid):
      return make_response(jsonify({"error":"movie ID already exists"}),409)
  movies.append(req)
  res = make_response(jsonify({"message":"movie added"},req,{
            "GET": {"href": "http://127.0.0.1:5000/movies/" + movieid},
            "PUT": {"href": "http://127.0.0.1:5000/movies/" + movieid},
            "POST": {"href": "http://127.0.0.1:5000/movies/" + movieid},
            "DELETE": {"href": "http://127.0.0.1:5000/movies/" + movieid}}),200)
  return res

#Modifie un film
@app.route("/movies/<movieid>", methods=["PUT"])
def update_movie(movieid):
  for movie in movies:
    if str(movie["id"]) == str(movieid):
      movie = request.get_json()
      res = make_response(jsonify({"message":"movie modified"},request.get_json(),{
        "GET": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},
        "PUT": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},
        "POST": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},
        "DELETE": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]}}),200)
      return res
  res = make_response(jsonify({"error":"movie ID not found"}),201)
  return res

#Delete un film
@app.route("/movies/<movieid>", methods=["DELETE"])
def del_movie(movieid):
  for movie in movies:
    if str(movie["id"]) == str(movieid):
      movies.remove(movie)
      return make_response(jsonify({"message":"movie deleted"},{"POST": {"href": "http://127.0.0.1:5000/movies/"}}),200)
  res = make_response(jsonify({"error":"movie ID not found"}),400)
  return res


if __name__ == "__main__":
  app.run()
