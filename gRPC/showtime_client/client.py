import grpc
import showtime_pb2
import showtime_pb2_grpc

def get_list_showtimes(stub):
    allShowtimes = stub.GetListShowtimes(showtime_pb2.Empty())
    for schedule in allShowtimes:
        print(schedule)
        #print("Showtimes called %s" % (schedule.date))

def run():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)
        print("-------------- GetListShowtimes --------------")
        get_list_showtimes(stub)

if __name__ == '__main__':
    run()