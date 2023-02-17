import serial
import time
import matplotlib
import numpy
#data sheet
data_sheet = [
"QID",
"QSID",
"QVFW",
"QVFW2",
"QPIRI",
"QFLAG",
"QPIGS",
"QPGSn",
"QMOD",
"QPIWS",
"QMCHGCR",
"QMUCHGCR",
"QOPM",
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

ser = serial.Serial('COM6', 2400)

buff = []
data_out = []
buff_join_v1 = []
buff_join_v2 = []
find_end = 1
try_data = int(input("시행 횟수: "))


f = open("data_out.txt", 'w')
f.write("\t---------------TEST START---------------\n")
f.close()

f = open("data_out.txt", 'a')

for i in range(try_data):
    for i in range(len(data_sheet)): #data_sheet의 수 만큼 반복.



    
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
            ser.write(ord_byte1[y])
            print(ord_byte1[y])

        while (find_end): #읽은 데이터 만큼 밤복

            buff_join = []
            data = ser.read()
            print(data)
            buff.append(data)

            if (data == b'\r'):
                find_end = 0

        #buff_join = ' '.join(i for i in buff)
        for n in range (len(buff)):
            buff_join_v1 += str(buff[n])

        buff_join_v2 = ' '.join(i for i in buff_join_v1)

        data_out.append(buff_join_v2)
    
    #txt에 저장
    for i in range(len(data_out)):

        sample_2=''
        sample = str(i+1) + ": " + data_out[i] + "\n"
        sample_1 = sample.replace("b ","")
        sample_2 = sample_1.replace("'","")
        print(sample_2)
        print(type(sample_2))
        f.write(sample_2)

        line = "\t---------------" + " complete" + "---------------" + '\n'
        f.write(line)

f.close()