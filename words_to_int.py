#!/usr/bin/env python

def word_int(lit):
	new_list = []
	for value in lit:
		result = 0
		for letter in value:
			result = result + 1
		new_list.append(result)
	return new_list

lister = ['high','five','little','person']
print word_int(lister)
