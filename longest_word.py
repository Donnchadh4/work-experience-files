#!/usr/bin/env python

def highest_number(listing):
        high_number = 0
        for number in listing:
                if number > high_number:
                        high_number = number
	return high_number

def longest_word(lit):
	new_list = []
	bigword = ""
	for word in lit:
		result = 0
		for letter in word:
			result = result + 1
		if result > highest_number(new_list):
			new_list.append(result)
			bigword = word
	return "the biggest word is %s which has a total letter count of %d." % (bigword,highest_number(new_list))

list_of_words = ["banging","mental","amazing","smashing"]
	
print longest_word(list_of_words)
