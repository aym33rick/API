import json
import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc

class MovieServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open('{}/databases/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

# def GetListBooking(self, request, context) :

    def GetBookingByUserID(self, request, context) :
        for booking in self.db:
            if booking['userid'] == request.userid:
                print("Booking found!")
                for date in booking['dates']:
                    for movie in date['movies']:
                        print(booking['userid'] , date['date'] ,movie)
                        yield booking_pb2.BookingData(BookingUserID=booking['userid'], date=date['date'], movies=movie)
        # yield booking_pb2.BookingData(BookingUserID="", date="", movies="")

# def PostBooking(self, request, context) :
#
# def PutBooking(self, request, context) :
#
# def DeleteBooking(self, request, context) :



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(MovieServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()