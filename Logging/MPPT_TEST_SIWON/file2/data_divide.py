import serial
buff_data = []

# 아두이노와의 시리얼 통신 설정
arduino_port = 'COM11'  # 아두이노 포트 (Windows의 경우 'COMx' 형식으로 변경)
baud_rate = 9600  # 시리얼 통신 속도

# 시리얼 포트 열기
ser = serial.Serial(arduino_port, baud_rate)

# 데이터 보내기
data_to_send = 'Hello Arduino!@'
encoded_data = data_to_send.encode('utf-8')  # UTF-8 인코딩
ser.write(encoded_data)  # 문자열을 바이트로 변환하여 보냄

while True :
            read = ser.read()
            
            #print(read)
            if read == b'@' :
                #print("*************************")
                break
            
            buff_data.append(read)

# 데이터 받기

# 받은 데이터 출력
#decoded_data = received_data.decode().strip()  # 바이트를 문자열로 변환하고 공백 제거
print('Received data:', buff_data)

# 시리얼 포트 닫기
ser.close()
