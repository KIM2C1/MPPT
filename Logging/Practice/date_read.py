import serial

ser = serial.Serial('COM11', 9600)

while(1):
    data = ser.read()
    print(data)

ser.close()