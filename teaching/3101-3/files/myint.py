class myint(int):
     def __add__(self, other):
         print "additon: {0} + {1}".format(self, other)
         return int.__add__(self, other)