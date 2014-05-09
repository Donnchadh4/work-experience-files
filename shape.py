#!/usr/bin/env python

class Shape:
	"""this class will be used to inherit to new object instances"""
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Square(Shape):
	#Must make an explicit call to the __init__ function in shape
	def __init__(self, side = 1, x= 0, y = 0):
		Shape.__init__(self,x,y)
		self.side = side

class Circle(Shape):
	#The same will be done here but with a circle
	def __init__(self, r = 1,x =0,y = 0):
		Shape.__init__(self,x,y)
		self.radius = r

firstSquare = Square()
print firstSquare.side
