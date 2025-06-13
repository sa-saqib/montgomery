


def karatfor8(A,B):   
    result = []
    a= [int(x,16) for x in A]    
    b= [int(x,16) for x in B]
    re=hex(a[0] * b[0]) #0xfe01
    if 2 < len(re) <5: #0x1
        result += str( re[2:]) , '00'
    elif 4 < len(re) <7:
        result = [ re[-2:] , re[2:-2]]
    
    return result

# x = [ '1f'] 
# y = [ '53']
# print(karatfor8(x, y))