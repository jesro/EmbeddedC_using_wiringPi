#Libraries
import socket
import RPi.GPIO as GPIO
import time

HOST = '192.168.1.7'
PORT = 65432

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def my_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting to connect client")
        s.bind((HOST,PORT))
        s.listen(5)
        conn, addr = s.accept()

        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024).decode('utf-8')
                if str(data) == "Data":
                    print("Sending Data...")
                    my_data = distance()
                    print("Measured Distance = %.1f cm" % my_data)
                    x_encoded_data = str(my_data).encode('utf-8')
                    conn.sendall(x_encoded_data)
                    #s.close()
                elif str(data) == "Quit":
                    print("SHutting server down")
                    s.close()
                    break
                if not data:
                    s.close()
                    break
                else:
                    s.close()
                    pass

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            my_server()
            #dist = distance()
            #print ("Measured Distance = %.1f cm" % dist)
            #time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
#    finally:
#        print("FInally CLeanup")
#        GPIO.cleanup()
