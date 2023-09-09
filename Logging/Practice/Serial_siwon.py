import serial
import time
import matplotlib
import numpy

#data sheet
data_sheet = [
"QID",
"QSID",
#"QVFW",
#"QVFW2",
#"QPIRI",
#"QFLAG",
#"QPIGS",
#"QPGSn",
#"QMOD",
#"QPIWS",
#"QMCHGCR",
#"QMUCHGCR",
#"QOPM",
]

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

#####################
buff = []
data_out = []
buff_join_v1 = []
buff_join_v2 = []
count = 0
find_end = 1
#####################

try_data = int(input("시행 횟수: "))


f = open("data_out.txt", 'w')
f.write("\t---------------TEST START---------------\n")
f.close()


ser = serial.Serial('COM11', 2400, write_timeout=3)

for i in range(try_data):
    
    for i in range(len(data_sheet)): #data_sheet의 수 만큼 반복.

        
        ord_byte1 = []
        order = data_sheet[i]
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
            ser.write(ord_byte1[y])  #보내는 값
            print(ord_byte1[y])

##########################################################################
        buff = []
        buff_join_v1 = []

        while (True): #읽은 데이터 만큼 반복
            try:
                data = ser.read()
                if data:
                    print("받은값:", data)
                    print("배열값", buff)
                    buff.append(data)
            except serial.SerialTimeoutException():
                print("time out")
                break

    print("다음****************")
"""
        #buff_join = ' '.join(i for i in buff)
        for n in range (len(buff)):
            buff_join_v1 += str(buff[n])

        buff_join_v2 = ' '.join(i for i in buff_join_v1)

        data_out.append(buff_join_v2)
    
    #txt에 저장
    for i in range(len(data_out)):
        f = open("data_out.txt", 'a')
        
        sample_2 = ''
        sample = str(data_out[i])

        sample_1 = sample.replace("b ","")
        sample_2 = sample_1.replace("'","")
        sample_3 = str(i+1) + ": " + sample_2 + "\n"

        f.write(sample_3)
        f.close()

    f = open("data_out.txt", 'a')
    line = "\t---------------" + " complete" + "---------------" + '\n'
    f.write(line)
    f.close()

f.close()
"""