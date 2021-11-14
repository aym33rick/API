import grpc
import user_pb2
import user_pb2_grpc

def get_user_by_ID(stub, userid):
    print(stub.GetUserByID(userid))

def get_booking_by_user_ID(stub, userid):
    bookings = stub.GetBookedMoviesOfUser(userid)
    for booking in bookings:
        print(booking)

def run():
  with grpc.insecure_channel('localhost:3004') as channel:
      stub = user_pb2_grpc.UserStub(channel)


      print("-------------- GetUserByID --------------")
      userid = user_pb2.UserId(userid="dwight_schrute")
      get_user_by_ID(stub, userid)

      print("-------------- GetBookingByUserID --------------")
      userid = user_pb2.UserId(userid="dwight_schrute")
      get_booking_by_user_ID(stub, userid)

if __name__ == '__main__':
  run()