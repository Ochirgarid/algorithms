#!/usr/bin/env python

"""
    File: triangle_area_solution-garid.py
    Find area and perimeter of rectangle
"""

__author__ = "Ochirgarid Chinzorig (Ochirgarid)"
__version__ = "1.0"

# Open file on read mode
inp = open("../test/test1.txt", "r")

# read input lines one by one
# and convert them to integer
a = int(inp.readline().strip())
b = int(inp.readline().strip())
c = int(inp.readline().strip())

# must close opened file
inp.close()

# calculate area
p = (a + b + c) * 0.5
area = p * (p - a) * (p - b) * (p - c)
area = area ** (.5)

# print for std out
print("Area : {}".format(area))
