"""
    *This program creates grid map for Assignment-4
    *Enter the number of row and column number that you want to create
"""

import sys
import random

fp = open("gameGrid.txt", "w")

letter_list = ["D","W", "S", "T"]
math_operation_list = ["|", "-", "+", "/", "\\"]

choose = int(input("Sadece harfler olsun istiyorsan 1'e bas: \n"
                   "Sadece matematik operatörleri olsun istiyorsan 2'ye bas: \n"
                   "Hem matematik operatörleri hem de harfler olsun istiyorsan 3'e bas: "))
if choose > 3 or choose < 1:
    print("Yanlış seçim")
else:
    row = int(input("Kaç satır olsun: "))
    column = int(input("Kaç sütun olsun: "))
    input_list = list()
    counter = 0
    if choose == 1:

        for i in range(row):
            tmp_list = list()
            for j in range(column+1):
                tmp_list.append(letter_list[random.randint(0, 3)])
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

    elif choose == 2:

        for i in range(row):
            tmp_list = list()
            for j in range(column+1):
                tmp_list.append(math_operation_list[random.randint(0, 4)])
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
    elif choose == 3:
        both_list = letter_list + math_operation_list
        for i in range(row):
            tmp_list = list()
            for j in range(column+1):
                tmp_list.append(both_list[random.randint(0, 8)])
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