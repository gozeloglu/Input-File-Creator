"""
    *This program creates grid map for Assignment-4
    *Enter the number of row and column number that you want to create
"""

import sys
import random

fp = open("gameGrid.txt", "w")

jewel_list = ["|", "-", "+", "/", "\\", "D","W", "S", "T"]


row = int(input("Row number: "))
column = int(input("Column number: "))
input_list = list()
counter = 0

for i in range(row):
    tmp_list = list()
    for j in range(column+1):
        tmp_list.append(jewel_list[random.randint(0, 8)])
    input_list.append(tmp_list)

for i in range(len(input_list)):
    counter = 0
    for j in range(len(input_list[i])):
        if counter == column:
            fp.write("\n")

        else:
            counter += 1
            fp.write(input_list[i][j])
            if counter != column:
                fp.write(" ")

fp.close()