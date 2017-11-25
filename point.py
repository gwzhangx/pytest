class Point:
	"""Represent a point in 2-D space"""
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return '(%d, %d)' % (self.x, self.y)
	
	def __str__(self):
		return '(%d, %d)' % (self.x, self.y)
	
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
