import time
from divide_file1 import MyStruct


data_C = "220.0 22.7 220.0 60.0 22.7 5000 5000 48.0 48.0 48.0 55.5 55.5 3 40 040 1 0 0 9 01 0 0 54.0 0 1 000 2"
data_E = "000.0 00.0 221.3 59.9 0087 0046 001 372 53.00 000 086 0036 0000 000.0 00.00 00000 00010000 00 00 00000 010"
data_F = "0 00000000000000 P 00 000.0 00.00 000.0 00.00 0000 0000 000 00.0 000 000 000.0 000 00000 00000 000 00000000 0 0 000 000 00 00 000"

##############################################
data_C_list = list(data_C.split())
for i, key in enumerate(MyStruct.QPIRI):
    MyStruct.QPIRI[key] = data_C_list[i]


for key, value in MyStruct.QPIRI.items():
    print(f"{key}: {value}")
print("#########################################")
###############################################
data_E_list = list(data_E.split())
for i, key in enumerate(MyStruct.QPIGS):
    MyStruct.QPIGS[key] = data_E_list[i]


for key, value in MyStruct.QPIGS.items():
    print(f"{key}: {value}")
print("#########################################")
###############################################
data_F_list = list(data_F.split())
for i, key in enumerate(MyStruct.QPGSn):
    MyStruct.QPGSn[key] = data_F_list[i]


for key, value in MyStruct.QPGSn.items():
    print(f"{key}: {value}")
print("#########################################")
###############################################

## QFLAG Divide
data_D = 'EbcvxzDajkuy'
exclude_chars = ['E', 'D']
data_D_list_E = []
data_D_list_D = []
i = 0
temp = 0

while i < len(data_D):
    if data_D[i] == 'E':
        temp = 0
        i += 1
    elif data_D[i] == 'D':
        temp = 1
        i += 1
    
    if temp == 0:
        data_D_list_E.append(data_D[i])
    elif temp == 1:
        data_D_list_D.append(data_D[i])
    i += 1

print(data_D_list_E)
print(data_D_list_D) 

