 
# from nextpower_of2 import nxtof2 
# from sub2hex import sub2hex
# from compare2hex import a_greaterthanb
from mulxr2 import mulwithr2 
from redc import redc
from karatfor256 import karatfor256
from karatfor384 import karatfor384
from karatfor528 import karatfor528

# curve = 
# 0 - P256
# 1 - P384
# 2 - P521
def montgomery(a,b,curve):

    if curve ==0:
        ar2 = mulwithr2(a,0)[:32]
        br2 = mulwithr2(b,0)[:32]
        aprime = redc(ar2,0)[:32]
        bprime = redc(br2,0)[:32]
        montmul= karatfor256(aprime,bprime)[:32]
        finmont= redc(montmul,0)[:32]
        result = redc(finmont,0)[:32]

    elif curve ==1:
        ar2 = mulwithr2(a,1)
        br2 = mulwithr2(b,1)
        aprime = redc(ar2,1)
        bprime = redc(br2,1)
        montmul= karatfor384(aprime,bprime)
        finmont= redc(montmul,1)
        result = redc(finmont,1)[:48]

    elif curve ==2:
        aprime = redc(a,2)
        bprime = redc(b,2)
        montmul= karatfor528(aprime,bprime)
        finmont= redc(montmul,2)
        result = redc(finmont,2)


    return result 


# a= ['fe', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff']
# b= ['3f', '41', '36', 'd0', '8c', '5e', 'd2', 'bf', '3b', 'a0', '48', 'af', 'e6', 'dc', 'ae', 'ba', 'fe', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff']


a=['01']
b=['01']
print(montgomery(a,b,0))



        



    

   


    


    

    


o=['ff','ff','ff','ff','ff','ff','ff','ff','00','00','00','00','00','00','00','00']
p=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']
# N=['ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', '00', '00', '00', '00',
#     '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', 'ff', 'ff', 'ff', 'ff']
print(montgomery(o,p,1))
    


