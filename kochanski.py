def kochanski_mul(x, y , R):
    bits_needed = R-1
    result = 0
    while x > 0:
        if x % 2 == 1:  
            result = (result + (y & bits_needed ))   & bits_needed
        x = x >> 1
        y = (y << 1) & bits_needed
 
    return result 
a= 0xffffffff00000002000000000000000000000001000000000000000000000001
b = 3356
c= pow(2,12)
#print(kochanski_mul(a,b,c))  

'''from lef8shift import l8s
from add2hex import add2hex



x= '101000000000000000000000000000001010000000000000000000000000000001100000000000000000000000000000000101111111111111111111111111111110011111111111111111111111111111010111111111111111111111111111110111111111111111111111111111111111000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000100000000000000000000000000000001'

res =[]
for i in range(len(x)):
    if int(x[i]) & 1 ==1:
        res.append(len(x)-1-i)
# print(res)

def kon(a): #[84, 01]
    final = ['00']*2
    for i in range(len(res)):
        final = add2hex(l8s(a,res[i]),final)
    return final


# a= ['84','01']
# print(kon(a))

'''