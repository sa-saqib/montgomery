


def mod(a,x):
    if x== 0:
        res = a[:32]
    elif x == 1:
        res = a[:48]
    elif x== 2:
        if (int(a[65],16)) & 1 == 1:
            res = a[:65] + ['01']
        else :
            res = a[:65] + ['00']

    return res 
        

