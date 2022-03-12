import unittest
from calc import Calc

obj = Calc()


class TestCalcAdd(unittest.TestCase):
    """
    Test the add function from the calc
    """

    def test_add_int(self):
        result = obj.add(3, 2)
        self.assertEqual(result, 5)

    def test_add_float(self):
        result = obj.add(3.3, 2)
        self.assertEqual(result, 5.3)

    def test_add_str(self):
        """
        concatenation
        """
        result = obj.add("aaa", "bbb")
        self.assertEqual(result, "aaabbb")


class TestCalcSubtract(unittest.TestCase):
    """
    Test the subtract function from the calc
    """

    def test_subtract_int(self):
        result = obj.subtract(3, 2)
        self.assertEqual(result, 1)

    def test_subtract_float(self):
        result = obj.subtract(3.5, 2)
        self.assertEqual(result, 1.5)


class TestCalcMultuply(unittest.TestCase):
    """
    Test the multiply function from the calc
    """

    def test_multiply(self):
        result = obj.multiply(3, 2)
        self.assertEqual(result, 6)


class TestDivide(unittest.TestCase):
    """
    Test the divide function
    """

    def test_divide_float(self):
        result = obj.divide(8.4, 2)
        self.assertEqual(result, 4.2)

    def test_divide_by_zero(self):
        """
        Test that multiplying integers returns the correct result
        """
        with self.assertRaises(ZeroDivisionError):
            obj.divide(8, 0)


if __name__ == "__main__":
    unittest.main()
