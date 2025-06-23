from bitstohex import from8
from into8bits import into8
from add2hex import add2hex
from karatfor256 import karatfor256
from sub2hex import sub2hex

def karatfor512(k, l) -> list :
    ''' inputs from 528 karat'''
    if len(k) <= 64:
        k = k + ((64-len(k))*['00'])
    if len(l) <= 64:
        l = l + ((64-len(k))*['00'])

    result4512 = []
    lowk = k [:32]
    lowl = l [:32]
    highk = k[32:]
    highl = l[32:]
    r512low = karatfor256(lowk, lowl)
    r512high = karatfor256(highk, highl)
    result4512 += (r512low[:32])

    x = add2hex(lowk, highk)
    y = add2hex(lowl, highl)
    if (len(x)) & (len(y)) == 33:
        x, y = x[:32], y[:32]
        midpat = karatfor256(x, y)
        # midpart = karatfor256( (add2hex(x, ['01'])), (add2hex(y, ['01'])) )
        # midm = sub2hex((sub2hex(midpart, midpat)),['01'])
        midx = ((add2hex(x, y)))
        midh = add2hex(midx, midpat[32:])
        mid = []
        # mid = add2hex((midpat[:32] + midh),(64*['00']+['01']) )
        mid = midpat[:32] + midh[:32] + add2hex(midh[32:], (['01']))

    elif (len(x) == 32) & (len(y) == 33):
        y = y[:32]
        midpat = karatfor256(x, y)
        # midpart = karatfor256( (add2hex(y, ['01'])), (x))
        # midm =sub2hex((sub2hex(midpart, midpat)),['01'])
        midm = x
        midh = add2hex(midm, midpat[32:])
        mid = []
        mid = midpat[:32] + midh

    elif (len(y) == 32) & (len(x) == 33):
        x = x[:32]
        midpat = karatfor256(x, y)
        # midpart = karatfor256( (add2hex(x, ['01'])), (y))
        # midm =sub2hex((sub2hex(midpart, midpat)),['01'])
        midm = y
        midh = add2hex(midm, midpat[32:])
        mid = []
        mid = midpat[:32] + midh

    else:
        mid = karatfor256(x, y)

    mid00 = (sub2hex(mid, (r512low)))
    mid0 = (sub2hex(mid00, (r512high)))
    mid1 = add2hex(mid0, r512low[32:])
    result4512 += (mid1[:32])
    result4512 += (add2hex(mid1[32:], r512high))
    return result4512


# f= ['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']

# g=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']

# f =['21', '9c', 'b0', '7d', '60', 'e3', 'c1', 'c1', 'ad', '3a', '5a', '9f', '51', 'cf', '47', '5d', 'fa', 'cc', '77', '5b', '99', '3a', 'ce', '6d', '1f', '42', '98', 'd9', '6c', 'b1', 'ea', 'ff',
#     '9d', '7a', '0e', 'ca', '7d', 'a1', 'be', 'fc', 'a0', '67', '04', 'f6', '25', '9a', 'a2', 'f5', '3c', 'fd', '38', '2c', '9f', 'd1', '74', 'ce', '09', '6c', 'd7', 'fb', '23', 'e1', 'fc', 'ea']
# g = ['45', 'aa', '34', 'cb', '3d', '9c', '5e', '7c', 'e8', '4b', 'f7', '08', '31', '92', '8b', '6f', '9c', '7b', 'b1', '7e', '22', 'bc', 'd3', 'f2', '84', 'c9', '2a', '07', 'f9', '12', 'd6', 'ff',
#       'bd', '8b', 'f5', '60', '50', '24', 'c9', 'a2', '3f', '0f', 'a0', '20', 'f4', 'fe', 'b7', 'b5', '44', '4a', 'f1', '9e', '3e', 'b3', '14', '0b', '91', '7a', '87', '79', 'c5', '04', '5c', 'f3']

# f = ['b7', 'f9', 'b0', 'f8', 'b0', '5b', '2d', '6f', '7b', '2d', '84', '4e', 'f0', '9c', '1e', 'af', '63', '3e', '76', '0a', '5c', '0e', '3e', 'f4', '0f', 'ea', '41', '8d', '64', '5f', '20', '3d',
#       'bc', '53', 'f0', 'b3', '9f', '14', 'bc', 'ba', '3a', 'd6', 'dc', 'f2', '85', '67', '4c', 'ff', '94', '01', 'fa', '9b', '6d', 'cb', 'ca', '4c', 'a1', 'd6', '12', '4c', '8c', '13', 'e4', '5a']
# g = ['c2', '3a', 'ae', 'ee', 'f3', 'ad', '30', '5c', '3b', '3f', '6f', '15', 'c2', 'e2', 'd2', '29', '6f', 'bb', 'a5', '24', '8c', 'df', '3d', '8a', 'b9', 'ec', 'bd', 'b0', '13', 'd8', 'e5', '11',
#       'c9', '91', '99', '70', 'df', '18', 'e5', '8d', 'b5', '4b', 'a2', '81', '7a', 'bc', 'ca', '34', '01', 'd9', '9f', '70', '46', 'a2', 'e1', '98', '8a', 'bc', '89', '0f', 'c9', 'd5', '15', '49']

# b=(karatfor512(f,g))
# a=(into8(hex(from8(f) * from8(g))[2:]))
# if a==b:
#     print("crct")
# else:
#     print('wrong')
#     print(a)
#     print(b)
