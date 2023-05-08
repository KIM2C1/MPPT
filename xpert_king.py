import serial
import time
import matplotlib
import numpy
import copy
import sys
import xlsxwriter
import datetime as date

command_table = [
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
    "QDI",
    "QMCHGCR",
    "QMUCHGCR",
    "QOPM"
]

ser = serial.Serial('COM11',2400) #set-com-port

modetype = input("T: 테스트 모드 / Q: 수동 모드: ")


#make crc16_xmodem
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


#data send part
def send_command(command) :        
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


        for y in range(len(ord_byte_en)) :
            ser.write(ord_byte_en[y])
            #print(ord_byte_en[y])
        #print('*************************')
        ######### 출력값이 16진수가 아닌 문자(기호)로 나오는 경우가 있는데 데이터 값은 같음 ###########


        #data reading part
        buff_data = []
        buff_str = []

        while True :
            read = ser.read()
            #print(read)
            if read == b'\r' :
                #print("*************************")
                break
            
            buff_data.append(read)

        for x in range (len(buff_data)):
               buff_str += str(buff_data[x])
            
        #print("buff_str: " ,buff_str)    
        output_data = ''.join(i for i in buff_str)
        pretty = output_data.replace("'b'", "").replace("'", "")
        return (pretty[1:])
        #print("FINAL: ",output_data)
        #print("FINAL-pro: ",output_data.replace("b", "").replace("'", "")) #output_data


#select
if modetype == 'T':
     #set file
     f = open("listup.txt", 'w')
     f.write("---------------TEST START---------------\n")
     f.close()
     f = open("listup.txt", 'a')

     trynumber = int(input("테스트 횟수: "))
     print("Testing...")
     start_time = time.time()

     #set xlsx
     workbook = xlsxwriter.Workbook('XPERT_KING_DATASHEET.xlsx')
     worksheet = workbook.add_worksheet()

     worksheet.write(0, 0, "COMMAND")
     worksheet.write(0, 1, "RECEIVE")
     xlsx_number = 1

     for trynumber_buff in range(trynumber):
          for command_table_buff in range(len(command_table)):
               command = command_table[command_table_buff] #find command in command_table
               data_out = send_command(command)            #send command   
               
               fault = 0
               number = command_table_buff+1               #check number 1, 2, ...
               numbering = '{:02d}'.format(number)         #translate number 01, 02, ...

               

               data_out_str = str(numbering) + ":   " + str(data_out) + "\n"
               f.write(data_out_str)

               end_time = time.time()

               #xlsx write
               worksheet.write(xlsx_number, 0, command_table[command_table_buff])
               worksheet.write(xlsx_number, 1, data_out)

               xlsx_number += 1

          #txt write
          log_time = date.datetime.now()    
          result = "-------------"+"ok:"+str(14-fault)+"/faile:"+str(fault)+"-------------\n"
          f.write(result)
          f.write("Time:" + str((end_time - start_time)) + "\t" + "Date:" + str(log_time) + "\n")
          f.write("\n")
        
          #xlsx write
          worksheet.write(xlsx_number, 0, "time:")
          worksheet.write(xlsx_number, 1, end_time - start_time)
          xlsx_number += 1

          worksheet.write(xlsx_number, 0,'')
          worksheet.write(xlsx_number, 1,'')
          xlsx_number += 1

     f.close()
     workbook.close()
     print("Test Complete!")


elif modetype == 'Q':
     #set xlsx
     workbook = xlsxwriter.Workbook('XPERT_KING_log.xlsx')
     worksheet = workbook.add_worksheet()
     worksheet.write(0, 0, "COMMAND")
     worksheet.write(0, 1, "RECEIVE")
     worksheet.write(0, 2, "TIME")

     buff = 1
     xlsx_number = 1
     
     while buff:
           command = input("command: ")
           if command == 'ESC':
                workbook.close()
                break
           else:
                data_out = send_command(command)


                log_time = date.datetime.now()
                print(log_time)
                worksheet.write(xlsx_number, 0, command)
                worksheet.write(xlsx_number, 1, data_out)
                worksheet.write(xlsx_number, 2, str(log_time))
                xlsx_number += 1

           print(data_out)