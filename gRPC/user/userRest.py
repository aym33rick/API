import grpc
import requests
from flask import Flask, make_response, jsonify, render_template, request
import json
import booking_pb2_grpc
import booking_pb2

app = Flask(__name__)

with open('{}/databases/users.json'.format("."), "r") as jsf:
  users = json.load(jsf)["users"]

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
  watched_movies = []
  #recuperation dans le service booking des films de cet user
  # à faire en gRPC
  resMovie = requests.get("http://localhost:5001/movies")
  movies = resMovie.json()
  with grpc.insecure_channel('localhost:3002') as channel:
    stub = booking_pb2_grpc.BookingStub(channel)
    useridbis = booking_pb2.BookingUserID(userid=userid)
    res = stub.GetBookingByUserID(useridbis)
    for booking in res:
      print(booking)
      for m in movies:
        if m['id'] == booking.movies:
          watched_movies.append(m)
          break
    return make_response(jsonify(watched_movies), 200)

if __name__ == "__main__":
  app.run()