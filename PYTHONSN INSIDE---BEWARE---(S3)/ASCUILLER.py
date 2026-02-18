# Python likes ASCILLs
from time import sleep as s
letter = input("Give me a letter!:")
print(f"The ASCILL number is {ord(letter)}!")
s(2)
value = int(input("Now give me an ASCILL value!:"))
print(f"The Letter is {chr(value)}!")
s(1)
while True:
    print(chr(value),end="")
