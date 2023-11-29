import unittest
import MathCode1

class TestMathMethods(unittest.TestCase):

    def test_add(self):
        assert MathCode1.add(1,2) == 3
        # self.assertEqual(3, MathCode1.add(1, 2))
        # self.assertEqual(10, MathCode1.add(3, 7))

    def test_multiply(self):
        self.assertEqual(50, MathCode1.multiply(5, 10))

    def test_power(self):
        self.assertEqual(256, MathCode1.power(2, 8))        

if __name__ == '__main__':
    unittest.main()
