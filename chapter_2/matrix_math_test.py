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

    def test_multiply_scalars(self):
        expected = [6]
        actual = matrix_math.multiply([3],[2])
        self.assertEqual(expected,actual)

    def test_multiply_vectors(self):
        expected = [11]
        actual = matrix_math.multiply([1,2],[[3],[4]])
        self.assertEqual(expected,actual)

    def test_multiply_n_x_n_matrix(self):
        expected = [[19,22],[43,50]]
        actual = matrix_math.multiply([[1,2],[3,4]],[[5,6],[7,8]])
        self.assertEqual(expected,actual)

    def test_multiply_non_n_x_n_matrix(self):
        expected = [[22,28],[49,64]]
        actual = matrix_math.multiply([[1,2,3],[4,5,6]],[[1,2],[3,4],[5,6]])
        self.assertEqual(expected,actual)

    def test_multiply_another_non_n_x_n_matrix(self):
        expected = [[6,4,2],[-2,0,2],[3,2,1]]
        actual = matrix_math.multiply([[0,2],[1,-1],[0,1]],[[1,2,3],[3,2,1]])
        self.assertEqual(expected,actual)

    # todo: handle case when 0 or a negative number is provided
    
    def test_identity_matrix_1(self):
        expected = [1]
        actual = matrix_math.identity_matrix(1)
        self.assertEqual(expected,actual)
    
    def test_identity_matrix_2(self):
        expected = [[1,0],[0,1]]
        actual = matrix_math.identity_matrix(2)
        self.assertEqual(expected,actual)

    def test_identity_matrix_3(self):
        expected = [[1,0,0],[0,1,0],[0,0,1]]
        actual = matrix_math.identity_matrix(3)
        self.assertEqual(expected,actual)
