import serial
import time

ser = serial.Serial("COM10", 9600) # 아두이노의 포트와 보율을 지정합니다.
a =[]
try:
    while(1):
      c = input("아두이노로 전송할 값: ")
      c = c.encode('utf-8')
      ser.write(c)

      time.sleep(1)
      for i in range(len(c)) :
          x = ser.readline()
          y = x.decode('utf-8').strip()
          a.append(y)
      for j in range(len(c)) :
          print(a[j], end ="")
      print("")
except KeyboardInterrupt:
    print("중지")