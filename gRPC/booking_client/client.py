import grpc
import booking_pb2
import booking_pb2_grpc


def get_list_booking(stub):
    bookings = stub.GetListBooking(booking_pb2.EmptyBooking())
    for booking in bookings:
        print(booking)

def get_booking_by_user_ID(stub, userid):
    bookings = stub.GetBookingByUserID(userid)
    for booking in bookings:
        print(booking)


def post_booking(stub, booking):
    stub.PostBooking(booking)
    print("Film added!")




def run():
  with grpc.insecure_channel('localhost:3002') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)

      print("-------------- GetListBooking --------------")
      get_list_booking(stub)

      print("-------------- GetBookingByUserID --------------")
      userid = booking_pb2.BookingUserID(userid="dwight_schrute")
      get_booking_by_user_ID(stub, userid)

      print("-------------- PostBooking --------------")
      booking = booking_pb2.BookingData(BookingUserID="chris_rivers",date="20151130",movies="720d006c-3a57-4b6a-b18f-9b713b073f3c")
      post_booking(stub, booking)

if __name__ == '__main__':
  run()