#!/usr/bin/env python

def inCommon(list1,list2):
	result = 0
	for i in list1:
		for f in list2:
			if i == f:
				result = result + 1
	return "there are %d values in common between the list" % result

