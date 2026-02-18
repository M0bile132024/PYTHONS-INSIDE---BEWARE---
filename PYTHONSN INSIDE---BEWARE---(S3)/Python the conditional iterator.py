# Python the conditional iterator

from time import sleep as s
#-------Functions----------
def loop(printa,wait=0.01,itera=1):
    global X
    X += itera
    print(printa)
    s(wait)
#-------Subroutines--------
def counting_loop():
    '''Write a program that outputs the numbers 1 to 100 using a while
    loop. '''
    global X
    while X <= 100:
        loop(X)
def repeat_output(num):
    '''Ask the user to enter a number. Repeat the phrase 'I am
    computing' that many times using a while loop. '''
    global X
    while X <= num:
        loop("I am computing")

#---------Program------------

#Task 1 – Counting with a loop
X = 1
counting_loop()

#Task 2 – Repeating output
X = 1
num = int(input("Please enter a number:"))
repeat_output(num)