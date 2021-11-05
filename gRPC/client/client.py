import grpc
import movie_pb2
import movie_pb2_grpc

def get_movie_by_id(stub,id):
    movie = stub.GetMovieByID(id)
    print(movie)

def get_movie_by_title(stub,title):
    movie = stub.GetMovieByTitle(title)
    print(movie)

def get_list_movies(stub):
    allmovies = stub.GetListMovies(movie_pb2.Empty())
    for movie in allmovies:
        print("Movie called %s" % (movie.title))

def delete_movie_by_id(stub,id):
    movie_deleted = stub.DeleteMovieByID(id)
    print("Movie Deleted!")

def post_movie(stub, movie_add):
    movie_added = stub.PostMovie(movie_add)
    print('Movie Added!')


def put_movie(stub, movie_put):
    stub.PutMovieByID(movie_put)
    print('Movie Modified!')


def run():
  with grpc.insecure_channel('localhost:3001') as channel:
      stub = movie_pb2_grpc.MovieStub(channel)

      print("-------------- GetMovieByID --------------")
      movieid = movie_pb2.MovieID(id = "a8034f44-aee4-44cf-b32c-74cf452aaaae")
      get_movie_by_id(stub, movieid)

      # print("-------------- GetMovieByTitle --------------")
      # movieTitle = movie_pb2.MovieTitle(title="Creed")
      # get_movie_by_title(stub, movieTitle)

      print("-------------- GetListMovies --------------")
      get_list_movies(stub)

      print("-------------- DeleteMovieByID --------------")
      delete_movie_by_id(stub, movieid)

      print("-------------- PostMovieByID --------------")
      movie_add = movie_pb2.MovieData(title="La soupe aux choux", rating=10,director="Louis de Funes", id="2")
      post_movie(stub, movie_add)

      print("-------------- PutMovieByID --------------")
      movie_put = movie_pb2.MovieData(title="The Good Dinosaur", rating=9.0, director="Moi", id="720d006c-3a57-4b6a-b18f-9b713b073f3c")
      put_movie(stub, movie_put)

if __name__ == '__main__':
  run()