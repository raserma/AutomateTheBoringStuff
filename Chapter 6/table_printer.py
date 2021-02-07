#!/usr/bin/env python3
# table_printer.py - this function only prints the 3 lists on 90 degrees.

def print_table(table):
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(2), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
print_table(tableData)
