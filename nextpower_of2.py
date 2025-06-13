def nxtof2(n): #['ff,'ff']
    a=[]
    f=n[-1]
    first=n[-1][0]
    if (int(first,16) >= 8):
        a= len(n)*['00']+ ["01"]
    else:
        f= int(f,16)
        f |= f >> 1
        f |= f >> 2
        f |= f >> 4
        f = hex(f+1)
        a= (len(n)-1)*['00']+ [f[2:]]

        
    return a

#0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff

# v= ['ff','01']
# print(nxtof2(v))




    

    
