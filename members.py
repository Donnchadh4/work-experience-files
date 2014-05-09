#!/usr/bin/env python

my_list = ["a","b","c","d"]
def member_checker(data,value):
	result = 0
	for i in data:
		if i == value:
			result = result + 1
	if result == 0:
		return "that value was not in the list"
	elif result == 1:
		return "that value was in the list"
	else:
		return "there was an error"

