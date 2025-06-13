#firstly, i thought of doing for each and every element of an array
# then, got the idea why do it, if it is repeating the same pattern for every (no of bits in element)
# again upon closer look you can see that the pattern is repeating for half of bits but looks some difficult to do it 
# lets see exmaple a= [ a2, b3, 93, 0d]   i.e., 0x0d 93 b3 a2        a= [ a2, b3, 93, 0d]       i.e., 0x0d 93 b3 a2
# a >>4 is     a>>4 = [ 3a, 3b, d9, 00]  i.e.,0x00 d9 3b 3a          a >>8= [ b3, 93, 0d, 00] i.e.,0x00 0d 93 b3     

from rightshift import rs

def ri8s(a,n):
    res=[]
    m1 = n>>3 #m1 = n//8
    m = n - (m1<<3)  #m=n%8
    if m==0:
        res = a[m1:] + m1*['00']     
    elif m==1:
        res = rs(a[m1:]) + m1*['00']
    elif m==2:
        re1 = rs(a[m1:])
        res = rs(re1) + m1*['00']
    elif m==3:
        re1 = rs(a[m1:])
        re2 = rs(re1)
        res = rs(re2) + m1*['00']
    elif m==4:
        re1 = rs(a[m1:])
        re2 = rs(re1)
        re3 = rs(re2)
        res = rs(re3) + m1*['00']
    elif m==5:
        re1 = rs(a[m1:])
        re2 = rs(re1)
        re3 = rs(re2)
        re4 = rs(re3)
        res = rs(re4) + m1*['00']
    elif m==6:
        re1 = rs(a[m1:])
        re2 = rs(re1)
        re3 = rs(re2)
        re4 = rs(re3)
        re5 = rs(re4)
        res = rs(re5) + m1*['00']
    elif m==7:
        re1 = rs(a[m1:])
        re2 = rs(re1)
        re3 = rs(re2)
        re4 = rs(re3)
        re5 = rs(re4)
        re6 = rs(re5)
        res = rs(re6) + m1*['00']

    return res

# a=['a2','b3','93','0d']
# print(ri8s(a,26))

