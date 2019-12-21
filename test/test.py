# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from numpy.testing import assert_array_equal
import doctest
import unittest

from Phoenix_interpol import sort



class SortTest(unittest.TestCase):
	def test(self):
		a = [3,5,0,1,2,4,6,7,8,9]
		c = [0,1,2,3,4,5,6,7,8,9]
		b = [1,2,3,4,5,6,7,8,9,0]
		d = [3,5,0,1,2,4,6,7,8,9]

		a1 = [9,3,5,0,1,2,4,6,7,8]
		c1 = [9,0,1,2,3,4,5,6,7,8]
		b1 = [0,1,2,3,4,5,6,7,8,9]
		d1 = [9,3,5,0,1,2,4,6,7,8]
    	
		a2,c2,b2,d2 = sort(a,c,b,d)

		assert_array_equal(a1,a2)
		assert_array_equal(b1,b2)
		assert_array_equal(c1,c2)
		assert_array_equal(d1,d2)



if __name__=='__main__':
	unittest.main()



 
