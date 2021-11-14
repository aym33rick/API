from flask import Flask, make_response, jsonify, render_template, request
import json

app = Flask(__name__)

with open('{}/databases/bookings.json'.format("."), "r") as jsf:
  bookings = json.load(jsf)["bookings"]

#Renvoie la page d'accueil du service
@app.route('/', methods=['GET'])
def index():
  return make_response("<h1 style='color:blue'>Welcome to the Booking service!</h1>",200)

#Renvoie un JSON contenant les times
@app.route('/bookings', methods=['GET'])
def json():
  return make_response(jsonify(bookings),200)

#Renvoie un film en fonction de son id
@app.route("/bookings/<userid>", methods=['GET'])
def get_booking_byid(userid):
  for booking in bookings:
    if str(booking["userid"]) == str(userid):
      res = make_response(jsonify(booking),200)
      return res
    return make_response(jsonify({"error":"booking ID not found"}),400)

#Crée un nouveau film
@app.route("/bookings/<userid>", methods=["POST"])
def add_booking_byuser(userid):
  req = request.get_json()
  for booking in bookings:
    #verifie si booking deja existant
    if str(booking["userid"]) == str(userid):
      for date in booking['dates']:
        if str(date['date']) == str(req.date):
          for movie in date['movies']:
            if str(movie) == str(req.movieid):
              return make_response(jsonify({"error":"booking ID already exists"}),409)
  #sinon ajoute le film
  newBooking = {}
  newBooking['userid'] = userid
  newBooking['dates'] = req
  bookings.append(newBooking)
  res = make_response(jsonify({"message":"booking added"}),200)
  return res

if __name__ == "__main__":
  app.run()