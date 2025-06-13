

def ls(a):
    b= [(int(x,16)) for x in a]
    re=[]
    re.append(format((((b[0]<<1) & 0xff)),"02x"))
    for i in range(1,len(a)):
        if b[i-1]>0x7f:
            z=((b[i]<<1) & 0xff) + 1
        else:
            z=((b[i]<<1) & 0xff)
      
        re.append(format((z),"02x"))
    if b[-1]>0x7f:
        re.append('01')   

    return re

# a=['00', '2e', '67', '01']
# # a=['01', '00', '00', '00', '01', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', 'fe', 'ff', 'ff', 'ff', 'fb', 'ff', 'ff', 'ff', 'fa', 'ff', 'ff', 'ff', 'fc', 'ff', 'ff', 'ff', '02', '00', '00', '00', '0c', '00', '00', '00', '14', '00', '00', '00', '14', '00', '00', '00']

# print(ls(a))


