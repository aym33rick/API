import grpc
import showtime_pb2
import showtime_pb2_grpc

def get_list_showtimes(stub):
    allShowtimes = stub.GetListShowtimes(showtime_pb2.Empty())
    for schedule in allShowtimes:
        print(schedule)

def get_times_bydate(stub, date):
    schedule = stub.GetTimesByDate(date)
    print(schedule)

def run():
    with grpc.insecure_channel('localhost:3003') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)

        print("-------------- GetListShowtimes --------------")
        get_list_showtimes(stub)

        print("-------------- GetTimesByDate --------------")
        date = showtime_pb2.Date(date="20151130")
        get_times_bydate(stub, date)

if __name__ == '__main__':
    run()