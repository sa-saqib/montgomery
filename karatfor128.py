from into8bits import into8
from add2hex import add2hex
from karatfor64 import karatfor64
from sub2hex import sub2hex
from bitstohex import from8

def karatfor128(g,h) -> list :
    ''' multiplies 128 bits, taken inputs from karat256 '''
    result4128 = []
    if len(g) <16 :
        g = g+ (16-len(g))*['00']
    if len(h) <16 :
        h = h+ (16-len(h))*['00']

    lowg  = (g)[:8]
    highg = (g)[8:]
    lowh  = (h)[:8]
    highh = (h)[8:]
    r128low = karatfor64(lowg, lowh)
    r128high = karatfor64(highg, highh)
    result4128+=(r128low[:8])

    x=add2hex(lowg,highg)
    y=add2hex(lowh,highh)

    if ((len(x) == 9) and (len(y)) == 9) :
        x, y = x[:8], y[:8]
        midpat = karatfor64(x,y)
        midx =  ((add2hex(x,y)))
        midh = add2hex( midx, midpat[8:])
        mid = []
        mid = midpat[:8] + midh[:8] + add2hex(midh[8:],(['01']))

    elif (len(x) ==8) and (len(y) == 9) :
        y = y[:8]
        midpat = karatfor64(x,y)
        # midpart = karatfor64( (add2hex(y, ['01'])), (x))
        # midm =(sub2hex(midpart, midpat))
        midm = x
        midh = add2hex( midm, midpat[8:])
        mid = []
        mid = midpat[:8] + midh

    elif (len(y) ==8) & (len(x) == 9) :
        x = x[:8]
        midpat = karatfor64(x,y)
        # midpart = karatfor64( (add2hex(x, ['01'])), (y))
        # midm =(sub2hex(midpart, midpat))
        midm = y
        midh = add2hex( midm, midpat[8:])
        mid = []
        mid = midpat[:8] + midh

    else:
        mid = karatfor64(x,y)

    mid00=  sub2hex(mid,r128low)
    mid0=  sub2hex(mid00,r128high)
    mid1 = add2hex(mid0,r128low[8:])
    result4128 +=(mid1[:8])
    result4128 +=(add2hex(mid1[8:],r128high))

    return result4128

# o=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']
# p=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']
# print(karatfor128(p,o))

# o=['ef','cd','ab','90','78','56','34','12','ef','cd','ab','90','78','56','34','12']
# p=['ef','cd','ab','90','78','56','34','12','ef','cd','ab','90','78','56','34','12']
# print(karatfor128(o,p))

# ans =into8((hex(0xffffffffffffffff90abcdef90abcdef * 0x90ffffffffffffffffabcdef90abcdef))[2:])
# o=['ef','cd','ab','90','ef','cd','ab','90','ff','ff','ff','ff','ff','ff','ff','ff']
# p=['ef','cd','ab','90','ef','cd','ab','ff','ff','ff','ff','ff','ff','ff','ff','90']
# v =(karatfor128(o,p)) #0x90ffffffffffffffc09d1d94419d1d935f249d6604d8fd8138a7053ba2f2a521
# print(ans,v)
# if ans ==v:
#      print('correct')
# else:
#      print('fail')

# f= ['1']
# g= [ '1']              #working
# print(karatfor128(f,g))

# f=['b2', '43', '2e', '1c', '6f', '95', 'a2', '7d', '1b', '0e', '1f', 'ac', '67', 'be', 'af', '94']
# g=['b7', '90', 'ac', '13', 'ad', 'e7', '45', '9f', 'cb', '84', '1e', 'e3', 'fa', 'd9', 'b0', '76']
# print(karatfor128(f,g))

# f=['3d', 'a7', 'c8', 'b1', 'b6', '42', 'd7', 'e3',
# '50', '6f', 'ab', 'd9', '1d', '7e', '92', 'a7']
# g= ['9e', 'f1', 'a2', 'd7', 'e5', 'cb', '03', '7f',
#  '14', '2c', '9e', '3d', 'a1', '67', 'eb', 'c8']
# print(karatfor128(f,g))
# ans=['3e','84','be','dc','ac','0d','59','80', 'd3', '0f', '8b', 'e4', '54', 'a9', '3d', 'cc',
#  '4e', '3c', '31', 'cd', '4a', '4c', 'e9', 'e7', '8d', '07', '8c', '60', '31', 'b9', 'ef', '44']

#'3e', '84', 'be', 'dc', 'ac', '0d', '59', '80', 'd3', '0f', '8b', 'e4', '54', 'a9', '3d', 'cc',
#  '4e', '3c', '31', 'cd', '4a', '4c', 'e9', 'e7', '8d', '07', '8c', '60', '31', 'b9', 'ef', '44']


# '3e', '84', 'be', 'dc', 'ac', '0d', '59', '80', 'd3', '0f', '8b', 'e4', '54', 'a9', '3d', 'cc',
#  '4f', '3c', '31', 'cd', '4a', '4c', 'e9', 'e7', '8d', '07', '8c', '60', '31', 'b9', 'ef', '44']

# x=['ef', 'ea', 'f6', 'cd', '25', 'd8', '79', '61', '6c', '7d', 'ca', '85', '85', '3c', '42', '3c']
# y= ['55', '82', '4f', 'eb', '92', 'b3', '49', '1e', 'e0', 'b0', 'bc', '20', '9c', '41', '9c', '3f']
# print(karatfor128(x,y))
# print(into8(hex(from8(x) * from8(y))[2:]))

# x=['f0', 'ea', 'f6', 'cd', '25', 'd8', '79', '61', '6c', '7d', 'ca', '85', '85', '3c', '42', '3c']
# y= ['56', '82', '4f', 'eb', '92', 'b3', '49', '1e',
#      'e0', 'b0', 'bc', '20', '9c', '41', '9c', '3f']


# x=['3d', 'a7', 'c8', 'b1', 'b6', '42', 'd7', 'e3',
#    '50', '6f', 'ab', 'd9', '1d', '7e', '92', 'a7']
# y= ['56', '82', '4f', 'eb', '92', 'b3', '49', '1e',
#      'e0', 'b0', 'bc', '20', '9c', '41', '9c', '3f']

# x=['3d', 'a7', 'c8', 'b1', 'b6', '42', 'd7', 'e3',
#    '50', '6f', 'ab', 'd9', '1d', '7e', '92', 'a7']
# y=['3d', 'a7', 'c8', 'b1', 'b6', '42', 'd7', 'e3',
#    '50', '6f', 'ab', 'd9', '1d', '7e', '92', 'a7']
# b=(karatfor128(y,x))
# a=(into8(hex(from8(x) * from8(y))[2:]))
# if a==b:
#     print("crct")
# else:
#     print('wrong')
#     print(a)
#     print(b)