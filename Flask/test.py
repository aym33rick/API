import json

print("hello")

with open('{}/databases/movies.json'.format("."), "r") as jsf:
  movies = json.load(jsf)["movies"]

print(movies)

for movie in movies:
    movie["links"]= {"self": {"href":"/movies/"+movie["id"]},"modify": {"href":"/movies/"+movie["id"]},"delete": {"href":"/movies/"+movie["id"]}}
    print(movie)


