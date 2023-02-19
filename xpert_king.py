import serial
import time
import matplotlib
import numpy
import copy
import sys

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
        ord_byte_en = []
        count = 0
        

        order = input('명령어를 입력하세요 : ')
        order_crc = order.encode('utf-8') # xmodem으로 바꿀 변수
        len_order = len(order) 
        order = list(order) 


        for x in range(len_order) : # ord_byte_en에 인코딩한 명령어 저장
            ord_byte_en.append(order[x].encode('utf-8'))


        crc = crc16_xmodem(order_crc) # xmodem으로 변환
        crc_hex = hex(crc) # 16진수로 표현
        crc_hex = list(crc_hex) 
        # print('crc_hex', crc_hex) 

        cr1 = '\\x' + crc_hex[2] + crc_hex[3] # 배열에서 16진수 1,2 자리 
        cr1_dc = copy.deepcopy(cr1)
        # print('cr1', cr1)

        cr2 = '\\x' + crc_hex[4] + crc_hex[5] # 배열에서 16진수 3,4 자리
        cr2_dc = copy.deepcopy(cr2)  

        cr1_b = cr1.encode().decode('unicode_escape').encode("raw_unicode_escape") # \\를 \로 출력하게 하는 인코딩 방식
        # print(cr1_b)
        cr2_b = cr2.encode().decode('unicode_escape').encode("raw_unicode_escape")
        # print(cr2_b)
        cr = '\r'.encode('utf-8')

        # 인코딩된 값들 모두 배열에 추가
        ord_byte_en.append(cr1_b) 
        ord_byte_en.append(cr2_b)
        ord_byte_en.append(cr)


        for y in range(len(ord_byte_en)) :
            ser.write(ord_byte_en[y])
            print(ord_byte_en[y])
        print('*************************')

        while True :
            read = ser.read()
            print(read)
        #   count += 1
        #   if read == '\r' :
        #      break


######### 출력값이 16진수가 아닌 문자(기호)로 나오는 경우가 있는데 데이터 값은 같음 ###########