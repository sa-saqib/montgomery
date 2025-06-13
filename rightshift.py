

def rs(a):
    b= [(int(x,16)) for x in a]
    re=[]
    for i in range(len(a)-1):
        # if b[i+1]&1 ==1:
        #     z=((b[i]>>1) | 1<<7)
        # else:
        #     z=(b[i]>>1)
        z=((b[i]>>1) | (1<<7)) if b[i+1]&1 ==1 else (b[i]>>1)
      
        re.append(format((z),"02x"))
    zl=(b[-1])>>1    
    re.append(format((zl),"02x"))

    return re

# a=['0d', '00', '00', '00']
# print(rs(a))