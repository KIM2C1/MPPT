import time
import serial

data_to_process = "(000.0 00.0 218.8 59.9 0065 0015 001 374 53.20 000 089 0035 0000 000.0 00.00 00000 00010000 00 00 00000 010[\xa2"
test_data = '45@'
protocol_item = ["Grid voltage", "Grid frequency", "AC output voltage", "AC output frequency", "AC output apparent power", "AC output active power", "Output load percent", "BUS voltage", "Battery voltage", "Battery charging curent", "Battery capacity", "Inverter heat sink temperture", "PV Input current for battery", "PV Input voltage 1", "Battery voltage from SCC", "Battery discharge curent", "Inverter status", "Battery voltage offset for fas on", "EEPROM version", "PV Charging power", "Inverter status"]

buff_data1 = []
buff_data = []
global num

# 아두이노와의 시리얼 통신 설정
arduino_port = 'COM11'  # 아두이노 포트 (Windows의 경우 'COMx' 형식으로 변경)
baud_rate = 9600  # 시리얼 통신 속도

# 시리얼 포트 열기
ser = serial.Serial(arduino_port, baud_rate)

encoded_data = test_data.encode('utf-8')  # UTF-8 인코딩
ser.write(encoded_data)  # 문자열을 바이트로 변환하여 보냄
read = ser.read()
current_word1 = ''

while read != b'@':
    if read != b' ':
        current_word1 += read.decode('utf-8')
    else:
        if current_word1 != '':
            buff_data1.append(current_word1)
            current_word1 = ''
    read = ser.read()

if current_word1 != '':
    buff_data1.append(current_word1)
    num = current_word1
    print(num)
# 받은 데이터 출력
print('Received data:', buff_data1)

ser.close()

current_word = ''
for char in data_to_process:
    if char == ' ':
        if current_word != '':
            buff_data.append(current_word)
            current_word = ''
    else:
        current_word += char

if current_word != '':
    buff_data.append(current_word)
    

#for index, (protocol_item, item) in enumerate(zip(protocol_item, buff_data)):
    #print(f"{protocol_item}: {item}")


#QPIGS<cr>: Inverter general status parameters inquiry
def QPIGS(data):
    print(protocol_item[data - 1] + ": " + str(buff_data[data - 1]))

def test():
    return num

while(1):
    #x = int(input("값을 일력하시오: "))
    #QPIGS(x)
    print(test())
    time.sleep(1)
