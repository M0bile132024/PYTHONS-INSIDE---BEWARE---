import time
import random
def waiting_dots(amount_of_dots = 3,waiting_time = 1):
    for i in range(amount_of_dots):
        print(".")
        time.sleep(waiting_time)
def Processing(Processing="Processing",amount_of_dots = 3,waiting_time = 1):
    print(Processing,end="")
    for i in range(amount_of_dots):
        print(".",end="")
        time.sleep(waiting_time)
    print("\nDone!")

