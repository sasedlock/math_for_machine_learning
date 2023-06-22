import chapter_2.matrix_math as matrix_math
import unittest

class Test_TestMatrixMath(unittest.TestCase):
    def test_validateArrayEquality(self):
        self.assertEqual([1,2],[1,2])

    def test_ValidateMatrixEquality(self):
        self.assertEqual([[1,2],[3,4]],[[1,2],[3,4]])

    def test_add_scalar(self):
        expected = [3]
        actual = matrix_math.add([1],[2])
        self.assertEqual(expected,actual)