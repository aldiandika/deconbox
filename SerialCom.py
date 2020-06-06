import serial
import time

counter = 32
ser = serial.Serial('COM4', 9600, timeout=1)

while True:

    # ser.write(str('A').encode())
    data = ser.readline().decode("utf-8")

    cek = str(data.split(' '))
    # rKotor, rShower, rBersih = cek.split(',')

    # data = ser.read()
    print(data)

    # if data == "A":
    #     print("data masuk")

    # time.sleep(1)  # Delay for one tenth of a second
