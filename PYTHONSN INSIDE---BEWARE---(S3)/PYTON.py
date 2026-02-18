# Iteration_Problems
# 1.Problem 1 – Count to Ten
from time import sleep
from numpy import mean
def count_to_ten():
   '''Write a program that prints the numbers 1 to 10 using a for loop.'''
   for i in range(10):
       print(i+1)
       sleep(0.1)
# Problem 2 – Times Table
def time_table(num):
    '''Ask the user for a number and print its times table from 1 to 12.'''
    for i in range(12):
        print(num*(i+1))
        sleep(0.1)
# Problem 3 – Sum of Numbers
def sum_of_nums(n):
    '''Ask the user for a number (n) and add the numbers from 1 to n. Print the total.'''
    j = 0
    for i in range(n):
        j += i+1
        print(j)
        sleep(0.1)
# Problem 4 – Repeated Input
def repeat_input(num_list):
    '''Use a for loop to ask the user for 5 numbers. Print the total and the average.'''
    print(sum(num_list))
    print(mean(num_list))
print("HELLO, I PYTON!")
sleep(2)
print("I COUNT TEN:")
sleep(2)
count_to_ten()
sleep(2)
NUM = int(input("NOW GIVE NUM:"))
print("I GIVE TIME TABLE:")
sleep(2)
time_table(NUM)
sleep(2)
NUM = int(input("GIVE MORE NUM:"))
print("I GIVE TRIANGLE NUM:")
sleep(2)
sum_of_nums(NUM)
NUM_LIST = []
for i in range(5):
    NUM = int(input("UGH< PYTON DEMAND MORE NUM!:"))
    NUM_LIST.append(NUM)
print("I GIVE SUM AND MEAN:")
sleep(2)
repeat_input(NUM_LIST)

