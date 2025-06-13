#this is actually not at all required, as we will no where be using this.
#itis because the inverse of n  w.r.t  R is 1.




from add2hex import add2hex
from karatfor520 import karatfor520
from karatfor8 import karatfor8
from sub2hex import sub2hex


def karatfor521(k,l):
    result=[]
    if (int(k[65],16)&0x1) & (int(l[65],16)&0x1) ==1:
        k,l = k[:64],l[:64]

        r521low = karatfor520(k,l)

        x=add2hex(k, ['01']) 
        y=add2hex(l, ['01'])


        midpart = karatfor520((add2hex(k, ['01'])), (add2hex(l, ['01'])))  

        midm = sub2hex((sub2hex(midpart, r521low)),['01']) 

        midh = add2hex( midm, r521low[64:])  




