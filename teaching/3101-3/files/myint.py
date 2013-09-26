#!/usr/bin/env python


class Number(object):
    def __init__(self, value=0):
        #print "num_init: {0}".format(value)
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class Conversion(object):
    def __init__(self, value=0):
        #print "conv_init: {0}".format(value)
        self.value = value

    def to_binary(self):
        return bin(self.value)

    def to_hex(self):
        return hex(self.value)


class MyInt(Number):
    #def __init__(self, value=0):
    #    Number.__init__(self, value)
    #    Conversion.__init__(self, value)

    def __add__(self, other):
        return MyInt(self.value + other.value)

    def __sub__(self, other):
        return MyInt(self.value - other.value)

    def __mul__(self, other):
        return MyInt(self.value * other.value)

    def __div__(self, other):
        return MyInt(self.value / other.value)

    def __eq__(self, other):
        return self.value == other.value

if __name__ == '__main__':
    print("== testing custom integer ==")
    i = MyInt(10)
    j = MyInt(20)
    k = MyInt(30)

    if (i + j) == k:
        print "testing succeeded for {0} and {1}".format(i, j)
    else:
        print "testing failed"

    #assert((MyInt(10) + MyInt(20)) == MyInt(30))
