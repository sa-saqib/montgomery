# from bitstohex import from8
# from into8bits import into8
from add2hex import add2hex
from karatfor128 import karatfor128
from karatfor256 import karatfor256
from sub2hex import sub2hex

def karatfor384(s, t) -> list :
    ''' direct inputs are taken '''
    result4384 = []
    if len(s) < 48:
        s = s + (48-len(s))*['00']
    if len(t) < 48:
        t = t + (48-len(t))*['00']

    lows = s[:32]
    lowt = t[:32]
    highs = s[32:]
    hight = t[32:]
    r384low = karatfor256(lows, lowt)
    r384high = karatfor128(highs, hight)
    result4384 += (r384low[:32])

    x = add2hex(lows, highs)
    y = add2hex(lowt, hight)
    if (len(x)) & (len(y)) == 33:
        x, y = x[:32], y[:32]
        midpat = karatfor256(x, y)
        # midpart = karatfor128( (add2hex(x, ['01'])), (add2hex(y, ['01'])) )
        # midm = sub2hex((sub2hex(midpart, midpat)),['01'])
        midx = ((add2hex(x, y)))
        midh = add2hex(midx, midpat[32:])
        mid = []
        # mid = add2hex((midpat[:32] + midh),(64*['00']+['01']) )
        # mid = midpat +  midm + ['01']
        mid = midpat[:32] + midh[:32] + add2hex(midh[32:], (['01']))

    elif (len(x) == 32) & (len(y) == 33):
        y = y[:32]
        midpat = karatfor256(x, y)
        # midpart = karatfor256( (add2hex(y, ['01'])), (x))
        # midm =((sub2hex(midpart, midpat)))
        midm = x
        midh = add2hex(midm, midpat[32:])
        mid = []
        mid = midpat[:32] + midh

    elif (len(y) == 32) & (len(x) == 33):
        x = x[:32]
        midpat = karatfor256(x, y)
        # midpart = karatfor256( (add2hex(x, ['01'])), (y))
        # midm =(sub2hex(midpart, midpat))
        midm = y
        midh = add2hex(midm, midpat[32:])
        mid = []
        mid = midpat[:32] + midh

    else:
        mid = karatfor256(x, y)

    mid00 = (sub2hex(mid, (r384low)))
    mid0 = (sub2hex(mid00, (r384high)))
    mid1 = add2hex(mid0, r384low[32:])
    result4384 += (mid1[:32])
    result4384 += (add2hex(mid1[32:], r384high))

    return result4384[:96]

# f=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
# 'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']
# g=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
# 'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']

# print(karatfor384(p,o))
# 7FA3D1C2B8479B6F215D9EA43B6F0C83
# A7927E1DD9AB6F50E3D742B6B1C8A73D
# 94AFBE67AC1F0E1B7DA2956F1C2E43B2
# f=['b2','43','2e','1c','6f','95','a2','7d','1b','0e','1f','ac','67','be','af','94','3d','a7','c8','b1','b6','42','d7','e3',
# '50','6f','ab','d9','1d','7e','92','a7','83','0c','6f','3b','a4','9e','5d','21','6f','9b','47','b8','c2','d1','a3','7f']
# g=['b2','43','2e','1c','6f','95','a2','7d','1b','0e','1f','ac','67','be','af','94','3d','a7','c8','b1','b6','42','d7','e3',
# '50','6f','ab','d9','1d','7e','92','a7','83','0c','6f','3b','a4','9e','5d','21','6f','9b','47','b8','c2','d1','a3','7f']

# 19F0C7D3A6B84E1F4DA59CE82A1F3D76
# C8EB67A13D9E2C147F03CBE5D7A2F19E
# 76B0D9FAE31E84CB9F45E7AD13AC90B7
# f=['b7','90','ac','13','ad','e7','45','9f','cb','84','1e','e3','fa','d9','b0','76','9e','f1','a2','d7','e5','cb','03','7f',
# '14','2c','9e','3d','a1','67','eb','c8','76','3d','1f','2a','e8','9c','a5','4d','1f','4e','b8','a6','d3','c7','f0','19']
# g=['b7','90','ac','13','ad','e7','45','9f','cb','84','1e','e3','fa','d9','b0','76','9e','f1','a2','d7','e5','cb','03','7f',
# '14','2c','9e','3d','a1','67','eb','c8','76','3d','1f','2a','e8','9c','a5','4d','1f','4e','b8','a6','d3','c7','f0','19']


# b=(karatfor384(g,f))
# a=(into8(hex(from8(f)*from8(g))[2:]))
# if a==b:
#     print("crct")
# else:
#     print('wrong')
#     print(a)
#     print(b)
