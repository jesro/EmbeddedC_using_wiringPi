import socket
import threading
import time


HOST = '192.168.1.7'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def process_data_from_server(x):
    return x


def my_client():
    #threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            my = "Data"

            my_inp = my.encode('utf-8')

            s.sendall(my_inp)
        
            data = s.recv(1024).decode('utf-8')

            dist = process_data_from_server(data)

            print("Measured Distance = %.1f cm" % float(dist))

            #s.close()
            time.sleep(2)


if __name__ == "__main__":
    try:
        while 1:
            my_client()
    except KeyboardInterrupt:
            print("Receiving Stopped")	
