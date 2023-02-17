import serial
import time
import matplotlib
import numpy
import copy
import sys
ord_byte = []
ord_byte1 = []
crc_sum = []

ser = serial.Serial('COM6',2400)

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

while True :        
        ord_byte = []
        ord_byte1 = []
        crc_sum = []
        # ser = serial.Serial(port = 'COM6', baudrate = 9600)
        order = input('명령어를 입력하세요 : ')
        order_byte = order.encode('utf-8') # xmodem으로 바꿀 변수
        len_order = len(order)
        order = list(order)

        for x in range(len_order) : # 
            ord_byte1.append(order[x].encode('utf-8'))

        crc = crc16_xmodem(order_byte)
        crc_hex = hex(crc)
        crc_hex = list(crc_hex)
        print('crc_hex', crc_hex) # crc hex 배열 출력
        cr1 = '\\x' + crc_hex[2] + crc_hex[3] # 배열에서 16진수 1,2 자리 
        cr1_dc = copy.deepcopy(cr1)
        print('cr1', cr1)
        cr2 = '\\x' + crc_hex[4] + crc_hex[5] # 배열에서 16진수 3,4 자리
        cr2_dc = copy.deepcopy(cr2)  
        cr1_b = cr1.encode().decode('unicode_escape').encode("raw_unicode_escape")
        #cr1_b = cr1.encode().decode('unicode_escape').encode('latin1')
        print(cr1_b)
        cr2_b = cr2.encode().decode('unicode_escape').encode("raw_unicode_escape")
        cr = '\r'.encode('utf-8')
        ord_byte1.append(cr1_b)
        ord_byte1.append(cr2_b)
        ord_byte1.append(cr)


        for y in range(len(ord_byte1)) :
            ser.write(ord_byte1[y])
            print(ord_byte1[y])
        print('*************************')
        while True :
            read = ser.read()
            print(read)


