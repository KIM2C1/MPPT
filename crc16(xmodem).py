import serial
def crc16_xmodem(data: bytes) -> int:
    crc = 0
    for b in data:
        crc ^= (b << 8)
        for i in range(8):
            if (crc & 0x8000):
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
    return crc & 0xffff
data2 = []
data = 'QID'
data1 = list(data)
for j in range(len(data)) :
    data2.append(data1[j].encode('utf-8'))
print(data2[0])
print(data2[1])
print(data2[2])

data = data.encode('utf-8')
crc = crc16_xmodem(data)
crc_hex = hex(crc)
crc_hex = list(crc_hex)
cr1 = '\\' + crc_hex[1] + crc_hex[2] + crc_hex[3]
cr2 = '\\' + 'x' + crc_hex[4] + crc_hex[5]  
cr1_b = cr1.encode('utf-8')
cr2_b = cr2.encode('utf-8')
cr = '\r'.encode('utf-8')
print(cr1_b)
print(cr2_b)
print(cr)
ser = serial.Serial(port = 'COM6', baudrate= 9600)

ser.write(cr1_b)
ser.write(cr2_b)
ser.write(cr)
a = b'\\xd6'
#a = a.encode('utf-8')
byte_str = b'\\xd6'
decoded_byte_str = byte_str.decode('unicode_escape').encode('utf-8')
print(decoded_byte_str)
byte_literal = '\\xff\\xd8\\xff'
byte_literal.decode('unicode_escape').encode('raw_unicode_escape')
print(byte_literal)