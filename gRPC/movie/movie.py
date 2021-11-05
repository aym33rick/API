import json
import grpc
from concurrent import futures
import movie_pb2
import movie_pb2_grpc

class MovieServicer(movie_pb2_grpc.MovieServicer):
    def __init__(self):
        with open('{}/databases/movies.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["movies"]

    def GetMovieByID(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                print("Movie found!")
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
        return movie_pb2.MovieData(title="", rating="", director="", id="")

    def GetMovieByTitle(self, request, context):
        for movie in self.db:
            if movie['title'] == request.title:
                print("Movie found !")
                return movie_pb2.MovieData(title=movie['title'],
                                       rating=movie['rating'],
                                       director=movie['director'],
                                       id=movie['id'])
        return movie_pb2.MovieData(title="", rating="", director="", id="")

    def GetListMovies(self, request, context):
        for movie in self.db:
            yield movie_pb2.MovieData(title=movie['title'], rating=movie['rating'],director=movie['director'], id=movie['id'])

    def DeleteMovieByID(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                print("Movie found and deleted!")
                self.db.remove(movie)
        return movie_pb2.Empty()

    #passe un movie et pas que l'id du con
    def PostMovie(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                print("MovieID already exist!")
                return movie_pb2.Empty()
        self.db.append(movie_pb2.MovieData(title=request.title, rating=request.rating,director=request.director, id=request.id))
        print("Movie added!")
        return movie_pb2.Empty()

    # A REVOIR
    def PutMovieByID(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                self.db.remove(movie)
                self.db.append(movie_pb2.MovieData(title=request.title, rating=request.rating, director=request.director,id=request.id))
                print("Movie found and Modified!")
                return movie_pb2.Empty()
            else:
                print("Movie not found !")
        return movie_pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_pb2_grpc.add_MovieServicer_to_server(MovieServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()