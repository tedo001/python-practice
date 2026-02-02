def dd(num):
    left=[]
    right=[]
    pivot=num[0]
    for j in num:
        if j>pivot:
            left.append(j)
        else:
            right.append(j)
    """
    sd=0
    for i in num:
        sd=sd+i
    if sd==pivot:
        return left
    else:
        return right
     """
    return [left+pivot+right]
print(dd([1,2,3]))


