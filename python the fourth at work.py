# Write your code here :-D
import time
Pounds = int(input("Hello, this is Python Exchanges, please enter how many pounds you wish to exchange:"))
What_to_convert_to = int(input("And what'd you wish to convert to? Press 1 for Indian Rupees, 2 for Chinese Yuan,3 for Niria , 4 for C/T or 5 for the internet FAMOUS bitcoin.Press 0 to keep your money and stop wasting time:"))
print("Processing")
time.sleep(3)
if What_to_convert_to == 1:
    Indian_rupeepee = Pounds * 105.75
    print("Alright , please go to the next till to collect your" , str(round(Indian_rupeepee,2)) , "Indian rupees! ;)")
elif What_to_convert_to == 2:
    CHINA_CURRENCY = Pounds * 9.04
    print("Alright , please go to the next till to collect your" , str(round(CHINA_CURRENCY,2)) , "Chinese yuan! ;)")
elif What_to_convert_to == 3:
    Niria = Pounds * 1,001.60
    print("Alright , please go to the next till to collect your" , str(round(Niria,2)) , "Niria! ;)")
elif What_to_convert_to == 4:
    C = Pounds * 1669.45
    T = C / 100
    print("Alright , please go to the next till to collect your" , str(round(C,2)) , "C or" , str(round(T,2)) , "T! ;)")
elif What_to_convert_to == 5:
    Bitcoin = Pounds * 0.33
    print("Alright , please go to the next till to collect your" , str(round(Bitcoin,2)) , "Bits! ;)")
else:
    print("... Why'd you still here?")
