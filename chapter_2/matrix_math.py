def add(a,b):
    """Adds two items together, whether they are a scalar, vector or matrix
    
    :a: first item to add, represented by a list
    :b: second item to add, represented by a list
    :return: result, represented by a list 
    """
    toReturn = []
    
    if len(a) != len(b):
        pass
    else:
        for i in range(len(a)):
            if type(a[i]) == list:
                ithRow = []
                for j in range(len(a[i])):
                    ithRow.append(a[i][j] + b[i][j])
                toReturn.append(ithRow)
            else:
                toReturn.append(a[i] + b[i])
    
    return toReturn

def multiply(a,b):
    """Multiplies two items together, whether they are a scalar, vector or matrix
    
    :a: first itme to multiply, represented by a list
    :b: second item to multiply, represented by a list
    :return: result, represented by a list
    """
    toReturn = []

    length_a = len(a)
    length_b = len(b)

    first_element_a = a[0]
    first_element_b = b[0]

    # if the length of both the inputs is just one, assume the alogithm is processing two scalars
    if length_a == 1 and length_b == 1:
        toReturn.append(first_element_a * first_element_b)
        return toReturn
    
    if length_a == length_b:
        # if the second input's first item is a list and it's length is 1, assume we are multiplying vectors
        if isinstance(first_element_b,list) and len(first_element_b) == 1:
            sum = 0
            for i in range(length_a):
                sum += a[i] * b[i][0]
            toReturn.append(sum)
        # else the second input is a list, and we're working with equal size matricies
        else:
            for i in range(length_a):
                ithRow = []
                for j in range(len(first_element_a)):
                    sum = 0
                    for k in range(len(first_element_a)):
                        sum += a[i][k] * b[k][j]
                    ithRow.append(sum)
                toReturn.append(ithRow)
    
    # TODO: can this logic be combined with the one above? 

    # else we're working with matricies of differing sizes
    else:
        for i in range(length_a):
            ithRow = []
            for j in range(len(first_element_b)):
                sum = 0
                for k in range(len(first_element_a)):
                    sum += a[i][k] * b[k][j]
                ithRow.append(sum)
            toReturn.append(ithRow)

    return toReturn

def identity_matrix(n):
    """Returns an identity matrix of size n x n
    
    :n: the size of the identity matrix to return
    :return: result, represented by a list
    """
    toReturn = []

    # starting from 0, create a row that's of length n
        # if the index for the current column is equal to the index of the current row, append 1, otherwise append 0
        # add this row to the return element
        # increment to the new row
    if n == 1:
        toReturn.append(1)

    else:
        for i in range(n):
            ithRow = []
            for j in range(n):
                if i == j:
                    ithRow.append(1)
                else:
                    ithRow.append(0)
            toReturn.append(ithRow)

    return toReturn

def associated_matrix(a, i, j = None):
    """Returns the associated matrix of matrix a with row index i and column index j
    
    :a: the matrix of which to find it's associated matrix
    :i: the row index to consider
    :j: the column index to consider
    :return: the associated matrix represented as a list of lists
    """
    toReturn = []

    if j is None:
        for l in range(len(a)):
            lthRow = []
            if l == 0:
                pass
            else:
                for k in range(len(a)):
                    if k == i:
                        pass
                    else:
                        lthRow.append(a[l][k])
                toReturn.append(lthRow)

    else:
        for k in range(len(a)):
            kthRow = []
            if k == i:
                pass
            else:
                for l in range(len(a)):
                    if l == j:
                        pass
                    else:
                        kthRow.append(a[k][l])
                toReturn.append(kthRow)

    return toReturn

def determinant(a):
    """Returns the determinant of a matrix
    
    :a: the matrix whose determinant to find
    :return: the determinant
    """
    # if we are working with a 2x2 matrix, return the calculation
    if len(a[0]) == 2 and len(a) == 2:
        return a[0][0]*a[1][1]-a[0][1]*a[1][0]

    # else, we are working with a larger matrix and must recurse
    # Take each value in the first row, and multiply it by the associated matrix's determinant
    else:
        det = 0
        
        for i in range(len(a[0])):
            assoc_matrix = associated_matrix(a, i)
            associated_matrix_determinate = determinant(assoc_matrix)
            if i % 2 == 0:
                det += (a[0][i] * associated_matrix_determinate)
            else:
                det -= (a[0][i] * associated_matrix_determinate)

        return det

def matrix_of_minors(a):
    """Returns a matrix's matrix of minors, as defined by Step 1 of https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
    
    :a: the matrix to invert
    :return: matrix of minors, represented by a list of lists
    """
    toReturn = []

    for i in range(len(a)):
        ithRow = []
        for j in range(len(a)):
            ithRow.append(determinant(associated_matrix(a,i,j)))
        toReturn.append(ithRow)

    return toReturn

def matrix_of_cofactors(a):
    """Returns a matrix's matrix of cofactors, as defined by Step 2 of https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
    
    :a: the matrix to find cofactors for
    :return: matrix of cofactors, represented by a list of lists
    """
    toReturn = []

    for i in range(len(a)):
        ithRow = []
        for j in range(len(a)):
            if i % 2 == 0:
                if j % 2 != 0:
                    ithRow.append(-a[i][j])
                else:
                    ithRow.append(a[i][j])
            else:
                if j % 2 == 0:
                    ithRow.append(-a[i][j])
                else:
                    ithRow.append(a[i][j])
        toReturn.append(ithRow)

    return toReturn

def transpose(a):
    """Returns a transposed version of the matrix passed in
    
    :a: the matrix to transpose
    :return: transposed matrix
    """
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i <= j:
                pass
            else:
                temp = a[j][i]
                a[j][i] = a[i][j]
                a[i][j] = temp
    
    return a

def divide_matrix(a,b):
    """Returns the result of multiplying each element in the input matrix by the input divisor
    
    :a: The matrix to be divided
    :b: The divisor
    :return: result, represented by a list of lists
    """

    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = (a[i][j] / b)
    
    return a

def inverse_matrix(a):
    """Returns the inverse of a matrix, if it can be found
    
    :a: the matrix to invert
    :return: result, represented by a list of lists
    """
    # Code modeled after algorithm described here: https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html

    # Step 1: Matrix of Minors
    mat_of_minors = matrix_of_minors(a)
    # Step 2: Matrix of Cofactors
    mat_of_cofactors = matrix_of_cofactors(mat_of_minors)
    # Step 3: Adjugate (aka transpose)
    transpose_mat = transpose(mat_of_cofactors)
    # Step 4: Multiply by 1/Determinant
    determinant_of_mat = determinant(a)
    return divide_matrix(transpose_mat,determinant_of_mat)

    