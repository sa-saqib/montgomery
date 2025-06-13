def kochanski_mul(x, y , R):
    bits_needed = R-1
    result = 0
    while x > 0:
        if x % 2 == 1:  
            result = (result + (y & bits_needed )) % R  
        x //= 2 
        y = (y * 2) % R
 
    return result 
a= pow(2,31)
b = 1
c= pow(2,33)
#print(kochanski_mul(a,b,c))  
