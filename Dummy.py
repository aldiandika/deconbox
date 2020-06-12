from time import sleep
import serial

from threading import Thread
# Establish the connection on a specific port
ser = serial.Serial('COM4', 9600, timeout=1)
counter = 32  # Below 32 everything in ASCII is gibberish
sleep(1)
ser.write(str('a').encode())
data = ser.readline()[:-2].decode()
# print(ser.readline()[:-2])  # Read the newest output from the Arduino

# while data == '':
#     ser.write(str('a').encode())
#     data = ser.readline()[:-2].decode()

# print(data)


class test:

    dataS = 0

    def func1(self):
        while True:

            ser.write(str('a').encode())
            data = ser.readline()[:-2].decode()
            print(data)

    Thread(target=func1).start()

    while True:
        print(dataS)
        sleep(1)

# from multiprocessing import Process

# def func1():
#     print('func1: starting')
#     for i in range(10000000):
#         pass
#     print('func1: finishing')


# def func2():
#     print('func1: starting')
#     for i in range(10000000):
#         pass
#     print('func1: finishing')


# if __name__ == '__main__':
#     p1 = Process(target=func1)
#     p1.start()
#     p2 = Process(target=func2)
#     p2.start()
#     p1.join()
#     p2.join()
