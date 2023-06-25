import serial
import time
import matplotlib
import numpy
import copy
import sys

#set-com-port
port = 'COM9'
baudrate = 2400

ser = serial.Serial(port,baudrate) 

#make send data using crc16_xmodem





#data send and decode
def send_command(command) :
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

        ord_byte_en = []
        count = 0

        order = command #input('명령어를 입력하세요 : ')
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

        buff_data = []
        for y in range(len(ord_byte_en)) :
            ser.write(ord_byte_en[y])
            print(ord_byte_en[y])
            #print(ser.read())
            #print(y)
            #read = ser.read()
            #print(read)
            #if (read != b'\r'):
                #buff_data.append(read)
            #else:
                #break   
        #print('*************************')
        ######### 출력값이 16진수가 아닌 문자(기호)로 나오는 경우가 있는데 데이터 값은 같음 ###########
        print("send complite!")

        #data reading part
        #buff_data = []
        buff_str = []


        
        for i in range(300):
                

        print("read complite!")
        for x in range (len(buff_data)):
               buff_str += str(buff_data[x])
               
        output_data = ''.join(i for i in buff_str)
        #print(output_data)
        pretty = output_data.replace("'b'", "").replace("'", "")  #데이터를 뽑으면 b' 가 포함되어있는데 b'를 지움

        #print(pretty)
        #print("--------------")
        buff_data = [] 

        #띄어쓰기를 기준으로 배열의 각 인덱스에 저장
        current_word = ''
        for char in pretty:
            if char == ' ':
                if current_word != '':
                    buff_data.append(current_word)
                    current_word = ''
            else:
                current_word += char
        
        if current_word != '':
            buff_data.append(current_word)

        return (buff_data)


test = []
test = send_command("QIPGS")
print(test[:])


