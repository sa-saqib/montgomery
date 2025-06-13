

def div(something, a):
    res=[]
    if a== 256:
        res= something[32:]
    if a== 384:
        res= something[48:]
    if a== 521:
        rs = (something[65:])
        
        
        b= [(int(x,16)) for x in rs]
        res=[]
        for i in range(len(rs)-1):
        # if b[i+1]&1 ==1:
        #     z=((b[i]>>1) | 1<<7)
        # else:
        #     z=(b[i]>>1)
            z=((b[i]>>1) | (1<<7)) if b[i+1]&1 ==1 else (b[i]>>1)
      
            res.append(format((z),"02x"))
        zl=(b[-1])>>1    
        res.append(format((zl),"02x"))

    return res





