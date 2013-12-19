__author__ = 'iury'
import unittest

def rabbits(n, k):
    if n == 2 or n == 1:
        return 1
    return rabbits(n-1, k) + (k * rabbits(n-2, k))



class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(19, rabbits(5,3))

    def test2(self):
        self.assertEqual(40,rabbits(6,3))

    def test3(self):
        self.assertEqual(2442624980786496, rabbits(36,5))

if __name__ == '__main__':
    unittest.main()



