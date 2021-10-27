import unittest
from timeit import default_timer
from sys import version_info
from findMissing2 import findMissing

class StringCalculatorTests(unittest.TestCase):
	
	def test_findMissing(self):
		missing = 60000123
		arr = list(range(100000000))
		arr.remove(missing)
		start_time = default_timer()
		result = findMissing(arr)
		end_time = default_timer()
		if version_info.major == 2:
			self.assertGreater(2, end_time-start_time)
		elif version_info.major == 3:
			self.asserGreater(2.5, end_time-start_time)
		self.assertEqual(missing,result)
