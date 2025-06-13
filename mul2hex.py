def mul_hex(a,b):
    maxlength = max(len(a),len(b))
    a= a + ['00']* (maxlength - len(a))
    b= b + ['00']* (maxlength - len(b))
    result=[]
    carry = 0
    for i in range(maxlength):
        x = int(a[i],16)
        for j in range (maxlength):
            y = int(b[j],16)
            MUL= x*y
        result.append(format(MUL,"04x"))


    

    return result



a=["ff","0a","ff"] 
#b=['01', '00', '00', '00', '01', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', 'fe', 'ff', 'ff', 'ff', 'fb', 'ff', 'ff', 'ff', 'fa', 'ff', 'ff', 'ff', 'fc', 'ff', 'ff', 'ff', '02', '00', '00', '00', '0c', '00', '00', '00', '14', '00', '00', '00', '14']
b= ['1','ff','f']
#print(mul_hex(a,b))

#fef b1e4 0bff