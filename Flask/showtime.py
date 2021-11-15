from flask import Flask, make_response, jsonify, render_template, request
import json

app = Flask(__name__)

with open('{}/databases/times.json'.format("."), "r") as jsf:
  times = json.load(jsf)["schedule"]

#Renvoie la page d'accueil du service
@app.route('/', methods=['GET'])
def index():
  return make_response("<h1 style='color:blue'>Welcome to the Showtime service!</h1>",200)

#Renvoie un JSON contenant les times
@app.route('/showtimes', methods=['GET'])
def json():
  return make_response(jsonify(times),200)

#Renvoie un film en fonction de son id
@app.route("/showmovies/<date>", methods=['GET'])
def get_times_bydate(date):
  for time in times:
    if str(time["date"]) == str(date):
      #movie["links"] = {"self": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]}, "modify": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]},"delete": {"href": "http://127.0.0.1:5000/movies/" + movie["id"]}}
      res = make_response(jsonify(time),200)
      return res
  return make_response(jsonify({"error":"Movie ID not found"}),400)

if __name__ == "__main__":
  app.run(port=5003)