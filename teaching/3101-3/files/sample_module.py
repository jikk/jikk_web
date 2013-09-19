""" A module to illustrate modules. 
"""
class A(object):
	def __init__(self, *args):
		self.args = args

def quadruple(x): 
	return x**4

x = 42

print("This is an example module. {0}".format(__name__))

if __name__ == "__main__":
	a = A(1, 2, 3)
	print("script mode")