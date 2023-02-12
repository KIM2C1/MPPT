import serial
import time

ser = serial.Serial("COM9", 9600) # 아두이노의 포트와 보율을 지정합니다.
try:
    while(1):
      c = input("아두이노로 전송할 값: ")
      c = c.encode('utf-8')
      ser.write(c)

      time.sleep(1)
      y = ser.readline()
      for i in range(len(c)):
        print("아두이노에서 받은 값:",y.decode('utf-8').strip())
        time.sleep(2)
        i += 1

except KeyboardInterrupt:
    print("중지")