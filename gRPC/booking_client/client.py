import grpc
import booking_pb2
import booking_pb2_grpc


# def get_list_booking(stub):


def get_booking_by_user_ID(stub, userid):
    bookings = stub.GetBookingByUserID(userid)
    for booking in bookings:
        print(booking)


# def post_booking(self, request, context):




def run():
  with grpc.insecure_channel('localhost:3002') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)

      print("-------------- GetBookingByUserID --------------")
      userid = booking_pb2.BookingUserID(userid="dwight_schrute")
      get_booking_by_user_ID(stub, userid)


if __name__ == '__main__':
  run()