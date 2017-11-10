#!/usr/bin/env python

"""
    File: pentagon_p_solution-garid.py
    Find the perimeter of pentagon.
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
d = int(inp.readline().strip())
e = int(inp.readline().strip())

# must close opened file
inp.close()

# calculate perimeter
p = a + b + c + d + e

# print for std out
print("Perimeter : {}".format(p))
