import serial
import time
ser = serial.Serial("COM6", 9600)
a = [b'Q',b'I',b'D',b'\xd6',b'\xea',b'\r']
a 
for i in range(len(a)):
    ser.write(a[i])
    print(a[i])

print('******************')
while True :
        x = ser.read()
        x = x.decode()
        print(x) 


