import serial
def gain():
    port = 'COM11'
    baudrate = 9600

    data_to_send = 'A'
    #print("A")
    ser = serial.Serial(port,baudrate)
    encoded_data = data_to_send.encode('utf-8')
    ser.write(encoded_data)
    print(ser.read())

gain()