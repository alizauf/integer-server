#!flask/bin/python
import unittest

#fibonacci
def fibonacci(n):
	a = 0
	b = 1
	sequence = []
	while len(sequence) < n:
		sequence.append(a)
		a = b
		b = sequence[-1] + a
	return sequence

#happy numbers, with a helper function for recursion
def happy(n):
	a = 1
	sequence = []
	while len(sequence) < n:
		reduced = happy_helper(a)
		if reduced:
			sequence.append(a)
		a += 1
	return sequence

def happy_helper(a):
	string_numerals = list(str(a))
	reduced = reduce(lambda x,y: x+y, map(lambda x:int(x)**2, string_numerals))
	if reduced == 1:
		return True
	#i read about happy numbers on wikipedia and learned all unhappy numbers reach this cycle
	elif reduced in [4, 16, 37, 58, 89, 145, 42, 20]:
		return False
	else: 
		return happy_helper(reduced)
		
#abundant numbers
def abundant(n):
	a = 1
	sequence = []
	while len(sequence) < n:
		filtered = reduce(lambda x,y: x+y, filter(lambda x: a % x == 0, range(1,a+1)))
		if filtered > 2 * a:
			sequence.append(a) 
		a += 1
	return sequence



class FunctionTests(unittest.TestCase):
	def test_fibonacci(self):
		self.assertEqual(fibonacci(1), [0])
		self.assertEqual(fibonacci(3),[0,1,1])
		self.assertEqual(fibonacci(10), [0,1,1,2,3,5,8,13,21,34])
		self.assertEqual(fibonacci(0), [])
		self.assertEqual(fibonacci(-1),[])

	def test_happy_helper(self):
		self.assertTrue(happy_helper(1))
		self.assertTrue(happy_helper(7))
		self.assertTrue(happy_helper(694))
		self.assertFalse(happy_helper(4))
		self.assertFalse(happy_helper(50))

	def test_happy(self):
		self.assertEqual(happy(1), [1])
		self.assertEqual(happy(3), [1,7,10])
		self.assertEqual(happy(10), [1,7,10,13,19,23,28,31,32,44])
		self.assertEqual(happy(0), [])
		self.assertEqual(happy(-1), [])

	def test_abundant(self):
		self.assertEqual(abundant(1), [12])
		self.assertEqual(abundant(3),[12,18,20])
		self.assertEqual(abundant(10), [12,18,20,24,30,36,40,42,48,54])
		self.assertEqual(abundant(0), [])
		self.assertEqual(abundant(-1),[])


if __name__ == '__main__':
     unittest.main()

