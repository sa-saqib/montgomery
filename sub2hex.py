def sub2hex(a,b):
    maxlength = max(len(a),len(b))
    a= a + ['00']* (maxlength - len(a))
    b= b + ['00']* (maxlength - len(b))
    result=[]
    carry = 0
    for i in range(maxlength):
        x = int(a[i],16)
        y = int(b[i],16)
        diff= x-y-carry
        
        if( diff < 0):
            diff = diff + 0x100
            
            carry = 1
        else :
            carry = 0
        result.append(format(diff&0xff,"02x"))


    return result

# a=['07', 'f7', '02']
# b= ["01"]
# print(sub2hex(a,b))

# b=['ff','f3', '1', '0'] 
# a=[ '0', '0', '2', '0']
# print(sub2hex(a,b))



