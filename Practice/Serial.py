import serial
import time

ser = serial.Serial("COM9", 9600) # 아두이노의 포트와 보율을 지정합니다.
try:
    while(1):
      c = input()
      c = c.encode('utf-8')
      ser.write(c)

      time.sleep(1)
      y = ser.readline()
      print(y.decode('utf-8').strip())

except KeyboardInterrupt:
    print("중지")