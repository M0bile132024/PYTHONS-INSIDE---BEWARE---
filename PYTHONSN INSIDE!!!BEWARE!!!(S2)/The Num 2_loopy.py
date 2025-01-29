# loopy
import time
import statistics as stat
import Python_the_Functions as PTF
def Dialogue(words):
    print(words)
    time.sleep(float(len(words.split()))*0.6)
the_num = int(input("GIVE ME YOUR NUM!:"))
PTF.Processing()
for i in range(12):
    if i == 0:
        print("The" , the_num , "times table is:")
    else:
        time.sleep(0.2)
        print(the_num*i)
time.sleep(3)
Dialogue("BUT IT'S STILL NOT ENOUGH NUM!!!!!")
the_num_list = []
for i in range(5):
    the_num_list.append(int(input("MORE NUM:")))
PTF.Processing()
try:
    the_num_list_mode = str(stat.mode(the_num_list))
except:
    the_num_list_mode = None
the_num_list_median = str(stat.median(the_num_list))
the_num_list_mean = str(stat.mean(the_num_list))
Dialogue("Intresting...")
Dialogue(f"The mode of your nums are {the_num_list_mode} , the median {the_num_list_median} , and the mean {the_num_list_mean}...")
Dialogue("Quite intresting I must say...")
Dialogue("BUT STILL NOT ENOUGH NUM!!!!")
starter_num = int(input("GIVE ME A STARTING NUM:"))
ender_num = int(input("GIVE ME A ENDING NUM:"))
PTF.Processing("Processi-",0,0)
for i in range(starter_num,ender_num):
    Dialogue("The fog is coming")
PTF.waiting_dots(3,0.5)
Dialogue("Oh No...")
Dialogue("My desire for the num has awakened the demon within me...")
Dialogue("I must the perform the anicent num rituals:")
for i in range(100):
    if (i+1) % 3 == 0 and (i+1) % 5 == 0:
        print("FIZZBUZZ")
    elif (i+1) % 3 == 0:
        print("FIZZ")
    elif (i+1) % 5 == 0:
        print("BUZZ")
    else:
        print(f"Performing ancient num ritual step {i+1} out of 100...")
        time.sleep(0.1)
PTF.waiting_dots(3,2)
Dialogue("Oh no no....")
Dialogue("The demon-it has already escaped....")
one_more_num = int(input("One more num, for my farewell pls...:"))
Dialogue("*insert exaggerated explosion sounds*")
def Asterisk_pyramid(one_more_num):
    num = one_more_num
    n = 1
    for i in range(1,one_more_num+1):
        for j in range(num):
            print(" ",end="")
        for k in range((n*2)-1):
            print("*",end="")
        for l in range(num):
            print(" ",end="")
        num -= 1
        n += 1
        print("\n")
        

Asterisk_pyramid(one_more_num) 

    





