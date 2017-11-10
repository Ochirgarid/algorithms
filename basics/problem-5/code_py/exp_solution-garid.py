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
x = int(inp.readline().strip())

# must close opened file
inp.close()

# calculate perimeter
y = x**2 + 2*x + 2340

# print for std out
print("Y : {}".format(y))
