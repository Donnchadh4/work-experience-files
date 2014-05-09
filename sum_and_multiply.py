#!/usr/bin/env python

def Summer(List):
	Sum = 0
	for value in List:
		
		if isinstance(value, int) == True:
			Sum = Sum + value
		else:
			return "error"
	return Sum

def multiplier(List):
	alter = 1
	for value in List:
		if isinstance(value, int) == True:
			alter = alter * value
		else:
			return "error"
	return alter

my_list = [1,2,3,4,5]
print Summer(my_list)
print multiplier(my_list)
