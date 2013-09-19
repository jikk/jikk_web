class FarmersMarket(object):
	def __init__(self, name, state, town, zipc):
		self.name = name 
		self.state,self.town,self.zipc = state,town,zipc 
	def __str__(self):
		return '{0} \n{1}, {2} {3}'.format(self.name, self.town, self.state, self.zipc)
	def __repr__(self):
		return 'FarmersMkt:<{0}:{1},{2} {3}>'.format(self.name, self.town, self.state, self.zipc)