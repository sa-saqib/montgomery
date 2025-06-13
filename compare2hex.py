def a_greaterthanb(a,b):
    if len(a)>len(b):
        return 1
    elif len(a)< len(b):
        return 0
    elif len(a) == len(b):
        a= [(int(x,16)) for x in a]
        b= [(int(x,16)) for x in b]

        for i in range (len(a)-1, -1, -1):
            if a[i] < b[i]:
                return 0
            elif a[i]> b[i]:
                
                return 1
        return 0




# a= ['ff','02','99']
# b= ['ff','01','99']
# print(a_greaterthanb(a,b))

