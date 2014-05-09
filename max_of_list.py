#!/usr/bin/env python

def max_of_list(lit):
	result = 0
	for i in lit:
		if i > result:
			result = i
	return result

print max_of_list([1,6,43,664,24])
