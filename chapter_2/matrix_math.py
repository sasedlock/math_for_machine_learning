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

    toReturn.append(a[0] * b[0])
    
    return toReturn