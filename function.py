#!/usr/bin/python

def circle(radius):
	if radius <= 2:
		return "too small"
	else:
		while radius > 40:
			radius = radius * 2
	return radius * radius * 3.14159

print circle(3)

for value in range(1,10):
	print "I am number %d." % value
