from bitstohex import from8
from into8bits import into8
from add2hex import add2hex
from karatfor512 import karatfor512
from karatfor16 import karatfor16
from sub2hex import sub2hex


def karatfor528(k, l) -> list:
    ''' direct inputs from 528 for 521  '''
    if len(k) < 66:
        k = k + ((66-len(k))*['00'])
    if len(l) < 66:
        l = l + ((66-len(k))*['00'])
    result4528 = []

    lowk = k[:64]
    lowl = l[:64]
    highk = k[64:]
    highl = l[64:]
    print("highk", highk)
    r528high = karatfor16(highk, highl)
    r528low = karatfor512(lowk, lowl)
    result4528 += (r528low[:64])

    x = add2hex(lowk, highk)
    y = add2hex(lowl, highl)

    # if (len(x)) & (len(y)) == 65:
    #     x, y = x[:64], y[:64]
    #     midpat = karatfor512(x, y)
    #     # midpart = karatfor512( (add2hex(x, ['01'])), (add2hex(y, ['01'])) )
    #     # midm = sub2hex((sub2hex(midpart, midpat)),['01'])
    #     midx = ((add2hex(x, y)))
    #     midh = add2hex(midx, midpat[64:])
    #     mid = []
    #     # mid = add2hex((midpat[:64] + midh),(128*['00']+['01']) )
    #     # mid = midpat +  midm + ['01']
    #     mid = midpat[:64] + midh[:64] + add2hex(midh[64:], (['01']))

    # elif (len(x) == 64) & (len(y) == 65):
    #     y = y[:64]
    #     midpat = karatfor512(x, y)
    #     # midpart = karatfor512( (add2hex(y, ['01'])), (x))
    #     # midm =sub2hex((sub2hex(midpart, midpat)),['01'])
    #     midm = x
    #     midh = add2hex(midm, midpat[64:])
    #     mid = []
    #     mid = midpat[:64] + midh

    # elif (len(y) == 64) & (len(x) == 65):
    #     x = x[:64]
    #     midpat = karatfor512(x, y)
    #     # midpart = karatfor512( (add2hex(x, ['01'])), (y))
    #     # midm =sub2hex((sub2hex(midpart, midpat)),['01'])
    #     midm = y
    #     midh = add2hex(midm, midpat[64:])
    #     mid = []
    #     mid = midpat[:64] + midh

    # else:
    #     mid = karatfor512(x, y)
    mid = karatfor512(x, y)

    mid0 = (sub2hex(mid, (r528low)))
    mid0 = (sub2hex(mid0, (r528high)))
    mid1 = add2hex(mid0, r528low[64:])
    result4528 += (mid1[:64])
    result4528 += (add2hex(mid1[64:], r528high))

    return result4528[:131]


# g= ['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','01']
# f=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','01']

# f=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','1f','ff','01']
# g = ['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff',
#      'ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','df','ff','01']
# b = (karatfor528(f, g))

# a = (into8(hex(from8(f) * from8(g))[2:]))
# if a == b:
#     print("crct")
# else:
#     print('wrong')
#     print(a)
#     print(b)
