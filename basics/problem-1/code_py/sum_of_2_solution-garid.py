#!/usr/bin/env python

"""
    File: sum_of_2_solution-garid.py
    Find sum of 2 integers
"""

__author__ = "Ochirgarid Chinzorig (Ochirgarid)"
__version__ = "1.0"

# Open file on read mode
inp = open("../test/test1.txt", "r")

# read input lines one by one
# and convert them to integer
a = int(inp.readline().strip())
b = int(inp.readline().strip())

# must close opened file
inp.close()

# calculate 2 number sum
c = a + b

# print for std out
print(c)
