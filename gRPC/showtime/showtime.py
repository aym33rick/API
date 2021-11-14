import json
import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc

class ShowtimeServicer(showtime_pb2_grpc.ShowtimeServicer):
    def __init__(self):
        with open('{}/databases/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]

    # retourne la liste des reservations
    def GetListShowtimes(self, request, context) :
        for showtime in self.db:
            yield showtime_pb2.ShowtimeData(date=showtime['date'], movies=showtime['movies'])

    # retourne la liste des reservations pour une date
    def GetTimesByDate(self, request, context) :
        for showtime in self.db:
            if showtime['date'] == request.date:
                return showtime_pb2.ShowtimeData(date=showtime['date'], movies=showtime['movies'])
        return showtime_pb2.ShowtimeData(date="", movies="")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowtimeServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()