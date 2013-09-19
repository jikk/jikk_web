class Complex(object):
	def __init__(self, x, y):
		self.x, self.y = x, y
	def __add__(self, other):
		return Complex(self.x + other.x, self.y + other.y)
	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self