#!/usr/bin/env python

def length_finder(string):
	x = 0
	for letter in string:
		x = x + 1
	return x
print length_finder("freefall")
