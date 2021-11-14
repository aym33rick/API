import json
import grpc
from concurrent import futures
import user_pb2
import user_pb2_grpc
import booking_pb2_grpc
import booking_pb2

class UserServicer(user_pb2_grpc.UserServicer):
    def __init__(self):
        with open('{}/databases/users.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["users"]

    def GetUserByID(self, request, context):
        for user2 in self.db:
            if user2['id'] == request.userid:
                print("User found!")
                return user_pb2.user(userid=user2['id'], name=user2['name'], last_active=str(user2['last_active']))

    def GetBookedMoviesOfUser(self, request, context):
        with grpc.insecure_channel('localhost:3002') as channel:
            stub = booking_pb2_grpc.BookingStub(channel)
            bookings = stub.GetBookingByUserID(booking_pb2.BookingUserID(userid=request.userid))
            print("Hello")
            for booking in bookings:
                yield user_pb2.BookingUserData(userid=booking.BookingUserID,date=booking.date,movies=booking.movies)
        return 0

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:3004')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
