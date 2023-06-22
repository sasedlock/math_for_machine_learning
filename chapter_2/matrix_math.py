def add(a,b):
    toReturn = []
    
    if len(a) != len(b):
        pass
    else:
        for i in range(len(a)):
            toReturn.append(a[i] + b[i])
    
    return toReturn