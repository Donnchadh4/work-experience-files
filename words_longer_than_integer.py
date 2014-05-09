#!/usr/bin/env python 

def integer(lit,Int):
	list_of_words = []
	for item in lit:
		result = 0
		for letter in item:
			result = result + 1
		if result >= Int:
			list_of_words.append(item)
	return list_of_words

my_list = ["sad","happy","excited","melancholy","frowny"]
integer(my_list,6)

