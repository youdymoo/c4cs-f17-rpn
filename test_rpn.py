import unittest
import rpn


class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("3 4 +")
        self.assertEqual(3, result)

    def test_subtract(self):
        result = rpn.calculate("9 5 -")
        self.assertEqual(3, result)

    def test_multiply(self):
        result = rpn.calculate("2 1 *")
        self.assertEqual(2, result)

    def test_divide(self):
        result = rpn.calculate("8 2 /")
        self.assertEqual(2, result)

    def test_malformed_input(self):
        result = rpn.calculate("1 2")
        self.assertEqual("Error: Malformed expression",result)
