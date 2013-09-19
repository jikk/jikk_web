import math

class Shape(object):
	def __init__(self, dimension, name):
		self.dimension = dimension
		self.name = name

	def __eq__(self, other):
		return self.area() == other.area()
	def __ne__(self, other):
		return not self.__eq__(other)

	def __cmp__(self, other):
		return self.area() - other.area()

	def perimeter(self):
		"""abstact method
		"""
		raise Exception("Abstract class invoked")

class Rectangle(Shape):
	def __init__(self, l, w):
			self.l, self.w = l, w
	def area(self):
		return self.l * self.w

class Square(Shape):
	def __init__(self, side, dimension, name):
		self.side = side
		Shape.__init__(self, dimension, name)

	def perimeter(self):
		return self.side ** 2


class Circle(Shape):
	def __init__(self, r, dimension, name):
		self.r = r
		Shape.__init__(self, dimension, name)
	def perimeter(self):
		return self.radius * 2 * math.pi
	def area(self):
		return self.r * 2 * math.pi

def get_perimeter(shape):
	"""
	"""
	if isinstance(shape, Shape):
		return shape.perimeter()
	else:
		raise Exception("Invalid type for shape arguement: {0}".format(type(shape)))

def get_perimeter_dt(shape):
	"""
	duck-typed get_perimeter()
	"""
	try:
		return shape.perimeter()
	except AttributeError:
		print("the object does not support perimeter()") 
		return 0
