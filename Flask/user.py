from flask import Flask, make_response, jsonify, render_template, request
import json

app = Flask(__name__)

with open('{}/databases/users.json'.format("."), "r") as jsf:
  users = json.load(jsf)["users"]

with open('{}/databases/bookings.json'.format("."), "r") as jsf:
  bookings = json.load(jsf)["bookings"]

with open('{}/databases/movies.json'.format("."), "r") as jsf:
  movies = json.load(jsf)["movies"]

#Renvoie la page d'accueil du service
@app.route('/', methods=['GET'])
def index():
  return make_response("<h1 style='color:red'>Welcome to the User service!</h1>",200)

#Renvoie un JSON contenant les users
@app.route('/users', methods=['GET'])
def json():
  return make_response(jsonify(users),200)

#Renvoie les infos de l'user en fonction de son id
@app.route("/user/<userid>", methods=['GET'])
def get_user_byid(userid):
  for user in users:
    if str(user["id"]) == str(userid):
      res = make_response(jsonify(user),200)
      return res
  return make_response(jsonify({"error":"User ID not found"}),400)

#Renvoie les films réservé par cet utilisateur
@app.route("/user/bookings/<userid>", methods=['GET'])
def get_booked_movies_of_user(userid):
  for booking in bookings:
    if str(booking["userid"]) == str(userid):
      bookingTableau = {}
      bookingTableau['userid'] = userid
      bookingTableau['dates'] = []
      for date in booking["dates"]:
        dateTableau = {}
        dateTableau['date'] = date['date']
        for movie in movies:
          if str(movie['id']) == str(date['movies'][0]):
            #ajouter les infos du movie dans le booking
            dateTableau['movies'] = movie
        bookingTableau['dates'].append(dateTableau)
      return make_response(jsonify(bookingTableau), 200)
  return make_response(jsonify({"error":"booking ID not found"}),400)

if __name__ == "__main__":
  app.run()