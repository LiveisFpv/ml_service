import grpc


def run():
    # я в душе не понимаю что я делаю
    channel = grpc.insecure_channel('server:13000')
    

if __name__ == "__main__":
    run()