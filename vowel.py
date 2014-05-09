#!/usr/bin/env python 

def vowel_checker(word):
	word = word.lower()
	
	if word[0] == "a":
		return True
	elif word[0] == "e":
		return True
	elif word[0] == "i":
		return True
	elif word[0] == "o":
		return True
	elif word[0] == "u":
		return True
	else: 
		return False


