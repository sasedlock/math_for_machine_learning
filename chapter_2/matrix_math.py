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

    # todo: get length of a and b since it's referenced so often

    # if the length of both the inputs is just one, assume the alogithm is processing two scalars
    if len(a) == 1 and len(b) == 1:
        toReturn.append(a[0] * b[0])
        return toReturn
    
    if len(a) == len(b):
        # if the second input's first item is a list and it's length is 1, assume we are multiplying vectors
        if isinstance(b[0],list) and len(b[0]) == 1:
            sum = 0
            for i in range(len(a)):
                sum += a[i] * b[i][0]
            toReturn.append(sum)
        # else the second input is a list, and we're working with equal size matricies
        else:
            for i in range(len(a)):
                ithRow = []
                for j in range(len(a[0])):
                    sum = 0
                    for k in range(len(a[0])):
                        sum += a[i][k] * b[k][j]
                    ithRow.append(sum)
                toReturn.append(ithRow)
    
    # todo: can this logic be combined with the one above? 

    # else we're working with matricies of differing sizes
    else:
        for i in range(len(a)):
                ithRow = []
                for j in range(len(b[0])):
                    sum = 0
                    for k in range(len(a[0])):
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

def associated_matrix(a, i):
    """Returns the associated matrix of matrix a with column index i
    
    :a: the matrix of which to find it's associated matrix
    :i: the column index to consider
    :return: the associated matrix represented as a list of lists
    """


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
        
        # i = 0      i                   i+1,i+1, i+1,i+2   i+2,i+1, i+2,i+2
        #            i
        det += (a[0][0] * determinant([[a[1][1],a[1][2]],[a[2][1],a[2][2]]]))
        # i = 1      i                   i   i-1  i  i+1    i+1     
        det -= (a[0][1] * determinant([[a[1][0],a[1][2]],[a[2][0],a[2][2]]]))
        det += (a[0][2] * determinant([[a[1][0],a[1][1]],[a[2][0],a[2][1]]]))

        # for i in len(a[0]):
        #     associated_matrix = associated_matrix(a, i)
        #     associated_matrix_determinate = determinant(associated_matrix)
        #     if i % 2 == 0:
        #         det += (a[0][i] * associated_matrix_determinate)
        #     else:
        #         det -= (a[0][i] * associated_matrix_determinate)

        return det



def inverse_matrix(a):
    """Returns the inverse of a matrix, if it can be found
    
    :a: the matrix to invert
    :return: result, represented by a list
    """
    # Code modeled after algorithm described here: https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html


    