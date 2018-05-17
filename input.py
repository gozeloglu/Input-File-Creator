"""
    *This program creates test cases to try Assignment-4
    *Just enter the grid map size and the number of how many you want to
    create test cases.
"""

import sys
import random

file = open("test_case.txt", "w")

n = int(input("How many coordinates do you want? "))
row = int(input("Rown number: "))
column = int(input("Column number: "))

for i in range(n):
    file.write(str(random.randint(0,row-1)))
    file.write(" ")
    file.write(str(random.randint(0, column-1)))
    file.write("\n")

file.write("E\n")

file.write(input("Enter your name: "))

file.close()