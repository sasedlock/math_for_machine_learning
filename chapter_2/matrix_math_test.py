import chapter_2.matrix_math as matrix_math
import unittest

class Test_TestMatrixMath(unittest.TestCase):
    def test_add_scalar(self):
        expected = [3]
        actual = matrix_math.add([1],[2])
        self.assertEqual(expected,actual)
    
    def test_add_vector(self):
        expected = [4,6]
        actual = matrix_math.add([1,2],[3,4])
        self.assertEqual(expected,actual)

    def test_add_matrix_n_x_n(self):
        expected = [[2,4,6],[8,10,12],[14,16,18]]
        actual = matrix_math.add([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(expected,actual)

    # todo: add test and code for case when addition cannot occur, such as when a m x n matrix is added to a i x j matrix and m!=i or n!=j

    def test_multiply_scalar(self):
        expected = [6]
        actual = matrix_math.multiply([3],[2])
        self.assertEqual(expected,actual)
    