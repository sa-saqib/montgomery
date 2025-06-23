from bitstohex import from8
from add2hex import add2hex
# from split import split
from karatfor128 import karatfor128
from sub2hex import sub2hex
from into8bits import into8

def karatfor256(I, J) -> list:
    ''' direct inputs from either 256 or (384 or 512 bit) '''
    result4256 = []

    if len(I) <= 32:
        I = I + (32-len(I))*['00']
    if len(J) <= 32:
        J = J + (32-len(J))*['00']

    # lowi = split(I)[0]
    # lowj = split(J)[0]
    lowi = I[:16]
    highi = I[16:]
    lowj = J[:16]
    highj = J[16:]

    # print(lowi)
    # print(lowj)
    r256low = karatfor128(lowi, lowj)
    # rm256low = (str(hex((from8(lowi)) * (from8(lowj))))[2:])
    # m256low = into8(rm256low)
    # print(r256low)
    # print(m256low)
    # if r256low == m256low :
    #      print("good with r256 low")
    # else:
    #      print("failed with r256 low k128 ")

    result4256 += (r256low[:16])

    r256high = karatfor128(highi, highj)

    x = add2hex(lowi, highi)
    y = add2hex(lowj, highj)
    # print(f' x: {x}')
    # print(f' y: {y}')
    # rm256mid = (str(hex((from8(x)) * (from8(y))))[2:])
    # m256mid = into8(rm256mid)

    if (len(x) == 17) and (len(y) == 17):
        x, y = x[:16], y[:16]
        midpat = karatfor128(x, y)
        # midpart = karatfor128( (add2hex(x, ['01'])), (add2hex(y, ['01'])))
        # midm = sub2hex((sub2hex(midpart, midpat)),['01'])
        midx = ((add2hex(x, y)))
        midh = add2hex(midx, midpat[16:])
        mid = []
        # mid = add2hex((midpat[:16] + midh),(32*['00']+['01']) )
        mid = midpat[:16] + midh[:16] + add2hex(midh[16:], (['01']))

    elif (len(x) == 16) & (len(y) == 17):
        y = y[:16]
        midpat = karatfor128(x, y)
        # midpart = karatfor128( (add2hex(y, ['01'])), (x))
        # midm =((sub2hex(midpart, midpat)))
        midx = x
        midh = add2hex(midx, midpat[16:])
        mid = []
        mid = midpat[:16] + midh

    elif (len(y) == 16) & (len(x) == 17):
        x = x[:16]
        midpat = karatfor128(x, y)
        # midpart = karatfor128( (add2hex(x, ['01'])), (y))
        # midm =((sub2hex(midpart, midpat)))
        midx = y
        midh = add2hex(midx, midpat[16:])
        mid = []
        mid = midpat[:16] + midh
    else:
        mid = karatfor128(x, y)

    # r256mid = mid
    # print(r256mid)
    # print(m256mid)
    # if r256mid == m256mid :
    #      print("good with r256 mid")
    # else:
    #      print("failed with r256 mid ")

    mid00 = (sub2hex(mid, (r256low)))
    # mmid00 = (str(hex(from8(mid) - (from8(r256low))))[2:])
    # mmid = into8(mmid00)
    # if mid00 == mmid :
    #      print("good with  mid")
    # else:
    #      print("failed with mid ")
    mid0 = (sub2hex(mid00, (r256high)))
    mid1 = add2hex(mid0, r256low[16:])
    result4256 += (mid1[:16])
    result4256 += (add2hex(mid1[16:], r256high))

    # print(r256low)
    # print(r256high)
    return result4256[:64]


# both halves add to one etxra
# p = ['ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff',
#      'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff']
# o = ['ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff',
#      'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff']
# # # # o=['1']
# b = (karatfor256(p, o))
# print(b)

# f= ['1']
# g= [ '1']              #working
# print(karatfor256(f,g))

# A7927E1DD9AB6F50E3D742B6B1C8A73D 94AFBE67AC1F0E1B7DA2956F1C2E43B2
# f=['b2', '43', '2e', '1c', '6f', '95', 'a2', '7d', '1b', '0e', '1f', 'ac', '67', 'be', 'af', '94',
#     '3d', 'a7', 'c8', 'b1', 'b6', '42', 'd7', 'e3', '50', '6f', 'ab', 'd9', '1d', '7e', '92', 'a7']
# # C8EB67A13D9E2C147F03CBE5D7A2F19E 76B0D9FAE31E84CB9F45E7AD13AC90B7
# g=['b7', '90', 'ac', '13', 'ad', 'e7', '45', '9f', 'cb', '84', '1e', 'e3', 'fa', 'd9', 'b0', '76',
#     '9e', 'f1', 'a2', 'd7', 'e5', 'cb', '03', '7f', '14', '2c', '9e', '3d', 'a1', '67', 'eb', 'c8']
# b=(karatfor256(f,g))
# a=(into8(hex(from8(f) * from8(g))[2:]))
# if a==b:
#     print("crct")
# else:
#     print('wrong')
#     print(a)
#     print(b)

# f3bdcae12f87f94a5e6c3298817b2ffe_eca9b72d94ef3bd5a5edb64910fa3e12
# cbf31a46903ac7ee55fe09dcba19d44d_d3478e9c81f26c319b2375080a91454f
# f = ['12', '3e', 'fa', '10', '49', 'b6', 'ed', 'a5', 'd5', '3b', 'ef', '94', '2d', 'b7', 'a9', 'ec',
#       'fe', '2f', '7b', '81', '98', '32', '6c', '5e', '4a', 'f9', '87', '2f', 'e1', 'ca', 'bd', 'f3']
# g = ['4f', '45', '91', '0a', '08', '75', '23', '9b', '31', '6c', 'f2', '81', '9c', '8e', '47', 'd3',
#       '4d', 'd4', '19', 'ba', 'dc', '09', 'fe', '55', 'ee', 'c7', '3a', '90', '46', '1a', 'f3', 'cb']
# b=(karatfor256(f,g))
# a=(into8(hex(from8(f) * from8(g))[2:]))
# if a==b:
#     print("crct")
# else:
#     print('wrong')
#     print(a)
#     print(b)


# both halves add to exact
# 5a83d64fc96b91d3e7c29f5b237bdc4a_48f19c3b91f67d4e3263a15178a60b1a
# 3c2a958e6ff310d146fa12c0be81de8e_142e8eabb47c1930a3eabf6890c63e55
# f = ['1a', '0b', 'a6', '78', '51', 'a1', '63', '32', '4e', '7d', 'f6', '91', '3b', '9c', 'f1', '48',
#       '4a', 'dc', '7b', '23', '5b', '9f', 'c2', 'e7', 'd3', '91', '6b', 'c9', '4f', 'd6', '83', '5a']
# g = ['55', '3e', 'c6', '90', '68', 'bf', 'ea', 'a3', '30', '19', '7c', 'b4', 'ab', '8e', '2e', '14',
#       '8e', 'de', '81', 'be', 'c0', '12', 'fa', '46', 'd1', '10', 'f3', '6f', '8e', '95', '2a', '3c']


# f = ['12', '3e', 'fa', '10', '49', 'b6', 'ed', 'a5', 'd5', '3b', 'ef', '94', '2d', 'b7', 'a9', 'ec',
#       'fe', '2f', '7b', '81', '98', '32', '6c', '5e', '4a', 'f9', '87', '2f', 'e1', 'ca', 'bd', 'f3']
# g = ['12', '3e', 'fa', '10', '49', 'b6', 'ed', 'a5', 'd5', '3b', 'ef', '94', '2d', 'b7', 'a9', 'ec',
#       'fe', '2f', '7b', '81', '98', '32', '6c', '5e', '4a', 'f9', '87', '2f', 'e1', 'ca', 'bd', 'f3']


# f = ['55', '3e', 'c6', '90', '68', 'bf', 'ea', 'a3', '30', '19', '7c', 'b4', 'ab', '8e', '2e', '14',
#       '8e', 'de', '81', 'be', 'c0', '12', 'fa', '46', 'd1', '10', 'f3', '6f', '8e', '95', '2a', '3c']

# g = ['12', '3e', 'fa', '10', '49', 'b6', 'ed', 'a5', 'd5', '3b', 'ef', '94', '2d', 'b7', 'a9', 'ec',
#       'fe', '2f', '7b', '81', '98', '32', '6c', '5e', '4a', 'f9', '87', '2f', 'e1', 'ca', 'bd', 'f3']
# b=(karatfor256(g,f))
# a=(into8(hex(from8(f) * from8(g))[2:]))
# if a==b:
#     print("crct")
# else:
#     print('wrong')
#     print(a)
#     print(b)
