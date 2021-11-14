import json
import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import showtime_pb2_grpc
import showtime_pb2


class BookingServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open('{}/databases/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    # rajouter le fait que si il n'y a pas de booking la fonction renvoie un booking vide
    def GetListBooking(self, request, context):
        for booking in self.db:
            for date in booking['dates']:
                for movie in date['movies']:
                    yield booking_pb2.BookingData(BookingUserID=booking['userid'], date=date['date'], movies=movie)

    def GetBookingByUserID(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.userid:
                print("Booking found!")
                for date in booking['dates']:
                    for movie in date['movies']:
                        yield booking_pb2.BookingData(BookingUserID=booking['userid'], date=date['date'], movies=movie)
            else:
                yield booking_pb2.BookingData(BookingUserID="", date="", movies="")

    def PostBooking(self, request, context):
        film_not_find = True
        with grpc.insecure_channel('localhost:3003') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            answer = stub.GetTimesByDate(showtime_pb2.Date(date=request.date))
            for movie in answer.movies:
                if movie==request.movies:
                    film_not_find = False
                    self.db.append(booking_pb2.BookingData(BookingUserID=request.BookingUserID, date=request.date, movies=request.movies))
            if film_not_find:
                print("Le film ne passe pas à cette date la!")
        return booking_pb2.EmptyBooking()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
