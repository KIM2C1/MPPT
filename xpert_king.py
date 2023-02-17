import serial
import time
import matplotlib
import numpy
ord_byte = []
ord_byte1 = []
crc_sum = []



def crc16_xmodem(order: bytes) -> int:
    crc = 0
    for b in order:
        crc ^= (b << 8)
        for i in range(8):
            if (crc & 0x8000):
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
    return crc & 0xffff



ser = serial.Serial(port = 'COM6', baudrate = 9600)
order = input('명령어를 입력하세요 : ')
order_byte = order.encode('utf-8') # xmodem으로 바꿀 변수
len_order = len(order)
order = list(order)

for x in range(len_order) :
    ord_byte1.append(order[x].encode('utf-8'))

crc = crc16_xmodem(order_byte)
crc_hex = hex(crc)
crc_hex = list(crc_hex)
cr1 = '\\x' + crc_hex[2] + crc_hex[3]
cr2 = '\\x' + crc_hex[4] + crc_hex[5]  
cr1_b = cr1.encode().decode('unicode_escape').encode("raw_unicode_escape")
cr2_b = cr2.encode().decode('unicode_escape').encode("raw_unicode_escape")
cr = '\r'.encode('utf-8')
ord_byte1.append(cr1_b)
ord_byte1.append(cr2_b)
ord_byte1.append(cr)


for y in range(len(ord_byte1)) :
    ser.write(ord_byte1[y])
    print(ord_byte1[y])



