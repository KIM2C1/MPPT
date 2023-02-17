import serial
import time
import crc16
# crc
def crc16(data: str, poly: hex = 0xA001) -> str:
    '''
        CRC-16 MODBUS HASHING ALGORITHM
    '''
    crc = 0xFFFF
    for byte in data:
        crc ^= ord(byte)
        for _ in range(8):
            crc = ((crc >> 1) ^ poly
                   if (crc & 0x0001)
                   else crc >> 1)

    hv = hex(crc).upper()[2:]
    blueprint = '0000'
    return (blueprint if len(hv) == 0 else blueprint[:-len(hv)] + hv)


""" b = crc16(example_str)
print(b) """
num = 0
ser = serial.Serial("COM6", 2400) # 아두이노의 포트와 보율을 지정합니다.
try:
    while(1):
      a = []
      c = input("아두이노로 전송할 값: ")
      crc_c = crc16(c)
      cr = '0D'
      order = c + crc_c + cr
      print('보낸 값 :', order)
      order_list = list(order)
      print(order_list)
      for i in range(len(order)) :
        print(i)
        order_list1 = order_list[i].encode('utf-8')
      ser.write(order_list)

      time.sleep(1)
      for i in range(len(order)) :
          x = ser.readline()
          print("aa")
          y = x.decode('utf-8').strip()
          a.append(y)
          result = ''.join(i for i in a)
      print("받은 값: ", result)
      print("")
except KeyboardInterrupt:
    print("중지")

