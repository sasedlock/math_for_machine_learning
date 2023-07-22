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
    
    # else we're working with matricies of differing sizes
    # else:
    #     for i in range(len(a)):
    #             ithRow = []
    #             for j in range(len(a[0])):
    #                 sum = 0
    #                 for k in range(len(a[0])):
    #                     sum += a[i][k] * b[k][j]
    #                 ithRow.append(sum)
    #             toReturn.append(ithRow)

    
    return toReturn