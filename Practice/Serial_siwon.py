import serial

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

ser = serial.Serial('COM11', 9600)

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
    for i in range(1): #data_sheet의 수 만큼 반복.

    #

    #
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

        sample = str(i+1) + ": " + data_out[i] + "\n"
        sample_1 = sample.replace("b ","")
        sample_2 = sample_1.replace("'","")
        print(sample_2)
        print(type(sample_2))
        f.write(sample_2)

        line = "\t---------------" + " complete" + "---------------" + '\n'
        f.write(line)

f.close()