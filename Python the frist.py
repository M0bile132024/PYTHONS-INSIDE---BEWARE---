# Write your code here :-)
#OK!!!

import time
date = time.ctime()
his_her_name = input("pls enter name:")
print("Hi!")
time.sleep(1)
print("I am a very intelligent Python!")
print("I can tell you the date for one day!")
time.sleep(2)
print(date)
time.sleep(5)
print("I know your name" , his_her_name , ".....")
time.sleep(2)
print("I know that you do Scrath....")
time.sleep(2)

print("I even know your family......")
time.sleep(2)

print("But know that my collection of data isn't complete..")
time.sleep(2)

age = input("I'm gonna need your age:")
home = input("Your home:")
school = input("And even your school:")
print(f"{his_her_name} aged " , age , " living at " , home , """
and an education at """ , school , "(oh you must be a lucky child!!!).......>)" )
time.sleep(5)
quit()
