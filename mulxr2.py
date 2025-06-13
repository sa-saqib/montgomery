#x' = redc(x * r^2) we are writing this code for computing that x*r^2  

from karatfor256 import karatfor256
from karatfor384 import karatfor384

#here a is prime number 
def mulwithr2(a,curve):
    result=[]
    if curve ==0:
        x = ['03', '00', '00', '00', '00', '00', '00', '00', 'ff', 'ff', 'ff', 'ff', 'fb', 'ff', 'ff', 'ff',
             'fe', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'fd', 'ff', 'ff', 'ff', '04', '00', '00', '00']
        result = karatfor256(a,x) #r^2mod n inthis case (x) =0x4fffffffdfffffffffffffffefffffffbffffffff0000000000000003
    elif curve ==1:
        x = ['01', '00', '00', '00', 'fe', 'ff', 'ff', 'ff', '00', '00', '00', '00', '02', '00', '00', '00', '00', '00', '00', '00', 'fe', 'ff', 'ff', 'ff', 
             '00', '00', '00', '00', '02', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00']
        result = karatfor384(a,x)
    elif curve ==2:     #as r is just one more than n, r^2 mod n will be 1. so...,
        result = a   

    return result

v=['01']
print(mulwithr2(v,0))