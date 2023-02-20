def intersections(arr1, n, arr2, m) :
    arrNew = []
    if n<=m:
        compArr = arr2
        secArr = arr1
    else:
        compArr = arr1
        secArr = arr2
    for i in secArr:
        if i in compArr:
            arrNew.append(i)
            compArr.remove(i)
    return arrNew


print(intersections([10, 10],2,[10],1))
        
    
