# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from numpy.testing import assert_array_equal
import doctest
import unittest
from numpy import argsort
import numpy as np

from Phoenix_interpol import sort, cut_cold


class Test(unittest.TestCase):
	def test_sort(self):
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


	def test_cut(self):
		num_comp = np.array([1,2])
		num = np.array([1,1,1,1,2,2,2,2])
		x = np.array([1,2,3,2,5,6,5,4])
		y = np.array([7,8,9,10,11,12,13,14])

		x1 = [1,2,5]
		num1 = [1,1,2]
		y1 = [7,8,11]

		x2,num2,y2 = cut_cold(x,num,y,num_comp)

		assert_array_equal(x1,x2)
		assert_array_equal(num1,num2)
		assert_array_equal(y1,y2)

if __name__=='__main__':
	unittest.main()




 
