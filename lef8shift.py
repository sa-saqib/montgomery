from leftshift import ls

def l8s(a,n):
    res=[]
    m1 = n>>3 
    m = n - (m1<<3)  
    if m==0:
        res = (m1)*['00'] + a     
    elif m==1:
        res = m1*['00'] + ls(a) 
    elif m==2:
        re1 = ls(a)
        res = m1*['00'] + ls(re1) 
    elif m==3:
        re1 = ls(a)
        re2 = ls(re1)
        res = m1*['00'] + ls(re2) 
    elif m==4:
        re1 = ls(a)
        re2 = ls(re1)
        re3 = ls(re2)
        res = m1*['00'] + ls(re3) 
    elif m==5:
        re1 = ls(a)
        re2 = ls(re1)
        re3 = ls(re2)
        re4 = ls(re3)
        res = m1*['00'] + ls(re4) 
    elif m==6:
        re1 = ls(a)
        re2 = ls(re1)
        re3 = ls(re2)
        re4 = ls(re3)
        re5 = ls(re4)
        res = m1*['00'] + ls(re5) 
    elif m==7:
        re1 = ls(a)
        re2 = ls(re1)
        re3 = ls(re2)
        re4 = ls(re3)
        re5 = ls(re4)
        re6 = ls(re5)
        res = m1*['00'] + ls(re6) 

    return res


# a=['2e', '67', '01']
# print(l8s(a,16))