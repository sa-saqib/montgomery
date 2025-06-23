# from bitstohex import from8
# from into8bits import into8
''' after getting converted to 8 bit chunks adding them'''


def add2hex(a, b) -> list:
    ''' adding two lists in hex'''
    maxlength = max(len(a), len(b))
    a = a + ['00'] * (maxlength - len(a))
    b = b + ['00'] * (maxlength - len(b))
    result = []
    carry = 0
    for i in range(maxlength):
        x = int(a[i], 16)
        y = int(b[i], 16)
        add = x+y+carry
        halfsum = add & 0xff
        if add > 0xff:
            # add = add - 0x100
            carry = 1
        else:
            carry = 0
        result.append(format(halfsum, "02x"))
    if carry > 0:
        result.append('01')

    return result


# c=['ff', 'ff']
# d= ['ff', 'ff']
# print(add2hex(c,d))

# p=['ef','cd','ab','90','ef','cd','ab','ff']
# o=['1']
# print(add2hex(o,p))

# f=['b2', '43', '2e', '1c', '6f', '95', 'a2', '7d', '1b', '0e', '1f', 'ac', '67', 'be', 'af', '94']
# g=['3d', 'a7', 'c8', 'b1', 'b6', '42', 'd7', 'e3', '50', '6f', 'ab', 'd9', '1d', '7e', '92', 'a7']
# a=(add2hex(f,g))
# b= (into8(hex(from8(f) + from8(g))[2:]))

# g=['b7', '90', 'ac', '13', 'ad', 'e7', '45', '9f', 'cb', '84', '1e', 'e3', 'fa', 'd9', 'b0', '76']
# h=['9e', 'f1', 'a2', 'd7', 'e5', 'cb', '03', '7f', '14', '2c', '9e', '3d', 'a1', '67', 'eb', 'c8']
# a=(add2hex(h,g))
# print(a)
# b= (into8(hex(from8(h) + from8(g))[2:]))
# if a==b:
#     print("crct")
# else:
#     print('wrong')

# End-of-file (EOF)
