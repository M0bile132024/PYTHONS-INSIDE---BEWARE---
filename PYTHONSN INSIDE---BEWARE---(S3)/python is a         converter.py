# ACTIVITY:Unit meausursement converter
from time import sleep as s
MEAUSUREMENT_LIST = ["Bit",
    "Nibble",
    "Byte",
    "Kilobyte",
    "Megabyte",
    "Gigabyte",
    "Terabyte",
    "Petabyte",
    "Exabyte",
    "Yattabyte"]
def unit_measurement_converter(meausursement,number,conversion):
    '''ask for meausursement+number+conversion+convert and print output'''
    if meausursement == 1:
        conversion_factors = [0,4,8,1024
print("This is a\n\n\n       converter")
s(2)
i = 1
for x in MEAUSUREMENT_LIST:
    print(f"{i}:{x}")
    i += 1
MEAUSUREMENT = int(input("Chose a\n\n\n     meausursement number to convert from:"))
NUMBER = float(input("Enter a\n\n\n      number to convert:"))
i = 1
for x in MEAUSUREMENT_LIST:
    print(f"{i}:{x}")
    i += 1
CONVERSION= int(input("Chose a\n\n\n     meausursement number to convert to:"))
print(f"The answer is\n\n\n         {unit_measurement_converter(MEAUSUREMENT,NUMBER,CONVERSION)}")
