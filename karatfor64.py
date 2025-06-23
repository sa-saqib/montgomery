''' karat algo for 64 -bit'''
from add2hex import add2hex
from karat432 import karat432
from sub2hex import sub2hex
from bitstohex import from8
from into8bits import into8

def karatfor64(e, f)  -> list:
    '''multiply 64-bit numbers'''
    result464 = []
    # if len(e) < 8:
    #     e = e + (8-len(e))*['00']
    # if len(f) < 8:
    #     f = f + (8-len(f))*['00']
    lowe = e[:4]
    lowf = f[:4]
    highe = e[4:]
    highf = f[4:]
    r64low = karat432(lowe, lowf)
    r64high = karat432(highe, highf)
    result464 += (r64low[:4])

    x = add2hex(lowe, highe)
    y = add2hex(lowf, highf)

    if (len(x)) & (len(y)) == 5:
        x, y = x[:4], y[:4]
        midpat = karat432(x, y)
        # midpart = karat432( (add2hex(x, ['01'])), (add2hex(y, ['01'])) )
        # midm = sub2hex((sub2hex(midpart, midpat)),['01'])
        midx = ((add2hex(x, y)))
        midh = add2hex(midx, midpat[4:])
        mid = []
        # mid = add2hex(((midpat[:4] + midh)),(8*['00']+['01']) )
        mid = midpat[:4] + midh[:4] + add2hex(midh[4:], (['01']))

    elif (len(x) == 4) & (len(y) == 5):
        y = y[:4]
        midpat = karat432(x, y)
        # midpart = karat432( (add2hex(y, ['01'])), (x))
        # # midm =((sub2hex(sub2hex(midpart, midpat)),['01'])  )
        # midm = ((sub2hex(midpart, midpat)))
        midm = x
        midh = add2hex(midm, midpat[4:])
        mid = []
        mid = midpat[:4] + midh
    elif (len(y) == 4) & (len(x) == 5):
        x = x[:4]
        midpat = karat432(x, y)
        # midpart = karat432( (add2hex(x, ['01'])), (y))
        # midm =((sub2hex(midpart, midpat)))
        midm = y
        midh = add2hex(midm, midpat[4:])
        mid = []
        mid = midpat[:4] + midh
    else:
        mid = karat432(x, y)

    mid00 = (sub2hex((sub2hex(mid, (r64low))),(r64high)))
    # mid0 = (sub2hex(mid00, (r64high)))
    mid1 = add2hex(mid00, r64low[4:])
    result464 += (mid1[:4])
    result464 += (add2hex(mid1[4:], r64high))

    return result464[:16]

# f = ['cd', '51', '4d', 'c8', 'd6', '53', '52', '12']
# g = ['82', '15', 'cb', 'f6', 'a7', 'c1', 'f6', '15']

# f=['ef','cd','ab','90','ef','cd','ab','90']
# g=['ef','cd','ab','90','ef','cd','ab','ff']

# f= ['1']
# g= [ '1']              #working

# f=['b2', '43', '2e', '1c', '6f', '95', 'a2', '7d']
# g= ['b7', '90', 'ac', '13', 'ad', 'e7', '45', '9f']

# f=['1b', '0e', '1f', 'ac', '67', 'be', 'af', '94']
# g=['cb', '84', '1e', 'e3', 'fa', 'd9', 'b0', '76']
# b =karatfor64(f,g)

# a=(into8(hex(from8(f) * from8(g))[2:]))
# if a==b:
#     print("crct")
# else:
#     print('wrong')
#     print(a)
#     print(b)
