class FlipDict(dict):
	"""A dictionary that can be inverted
	"""
	def flip(self):
		"""Return a dictionary of values to
		   sets of keys
		"""
		res = {}
		for k in self:
			v = self[k]
			if not v in res:
				res[v] = set()
			res[v].add(k)
		return res