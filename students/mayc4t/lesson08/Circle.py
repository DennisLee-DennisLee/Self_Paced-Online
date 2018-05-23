#!/usr/bin/env python

import math

class Circle:
    def __init__(self, r):
        self._r = r

    @classmethod
    def from_diameter(self, d):
        return self(d/2)

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("Radius can't be negative")
        self._r = val
    
    @property
    def diameter(self):
        return 2*self._r
    
    @diameter.setter
    def diameter(self, val):
        self.radius= val/2

    @property
    def area(self):
        return math.pi * (2*self.radius)

    def __str__(self):
        return "Circle with radius {}".format(self.radius)

    def __repr__(self):
        return "'Circle ({})'".format(self.radius)

    def __add__(self, other):
        r = self.radius + other.radius
        return Circle(r)
    def __mul__(self, other):
        if isinstance ( other, Circle):
            return Circle( self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __lt__(self, other):
        return (self.radius < other.radius)

    def __gt__(self, other):
        return (self.radius > other.radius)

    
    def __lt__(self, other):
        return (self.radius < other.radius)

    def __eq__(self, other):
        return(self.radius==other.radius)
    
    @staticmethod
    def sort_key(self):
        return(self.radius)


    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.radius += other.radius
            return self
        elif type(other)==int:
            self.radius += other
            return self
        else:
            raise Exception("invalid argument")
    def __imul__(self, other):
        if isinstance(other, Circle):
            self.radius *= other.radius
            return self
        elif type(other) == int:
            self.radius *= other
            return self
        else:
            raise Exception("invalid argument")
            
