#!/usr/bin/env python

class Circle:
	"""Create a circle with a given radius"""
	allCircles = []
	def __init__(self):
		self.radius = 3
		self.__class__.allCircles.append(self)
	def area(self):
		"""Determine the area of a Circle"""
		return self.radius * self.radius * 3.14159

circle1 = Circle()
circle2 = Circle()

circle1.radius = 4
circle2.radius = 5

print circle1.area()
print circle2.area()
