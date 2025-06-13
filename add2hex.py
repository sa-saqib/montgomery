def add2hex(a,b):
    maxlength = max(len(a),len(b))
    a= a + ['00']* (maxlength - len(a))
    b= b + ['00']* (maxlength - len(b))
    result=[]
    carry = 0
    for i in range(maxlength):
        x = int(a[i],16)
        y = int(b[i],16)
        sum= x+y+carry
        halfsum = sum & 0xff
        if (sum > 0xff):
        #sum = sum - 0x100
            
            carry = 1 
        else :
            carry = 0
        result.append(format(halfsum,"02x"))    

    if carry > 0:
        result.append('01')  

    return result  



# a=['ff', 'ff']
# b= ['ff', 'ff']
# print(add2hex(b,a))
#['01', '00', '00', '00', '01', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', 'fe', 'ff', 'ff', 'ff', 'fb', 'ff', 'ff', 'ff', 'fa', 'ff', 'ff', 'ff', 'fc', 'ff', 'ff', 'ff', '02', '00', '00', '00', '0c', '00', '00', '00', '14', '00', '00', '00', '14']
# print(add2hex(b,a))



# p=['ef','cd','ab','90','ef','cd','ab','ff']
# o=['1']
# print(add2hex(o,p))
