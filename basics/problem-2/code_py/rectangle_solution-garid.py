#!/usr/bin/env python

"""
    File: sum_of_2_solution-garid.py
    Find area and perimeter of rectangle
"""

__author__ = "Ochirgarid Chinzorig (Ochirgarid)"
__version__ = "1.0"

# Open file on read mode
inp = open("../test/test1.txt", "r")

# read input lines one by one
# and convert them to integer
L = int(inp.readline().strip())
W = int(inp.readline().strip())

# must close opened file
inp.close()

# calculate area & perimetr
area = L * W
per = 2 * L * W

# print for std out
print("Area : {}".format(area))
print("Perimetr : {}".format(per))
