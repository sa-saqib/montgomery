''' karatsuba algo for 32-bit'''
# from into8bits import into8
# from bitstohex import from8
from add2hex import add2hex
from karat416 import karat416
from sub2hex import sub2hex
def karat432(c, d) -> list:
    ''' takes inputs from karatfor64, multiply 32-bit numbers'''
    # if len(c) <4 :
    #     c = c+ (4-len(c))*['00']
    # if len(d) <4 :
    #     d = d+ (4-len(d))*['00']

    result432 = []
    lowa = (c)[:2]
    lowb = (d)[:2]
    higha = (c)[2:]
    highb = (d)[2:]
    r32low = karat416(lowa, lowb)
    result432+=(r32low[:2])
    r32high = karat416(higha, highb)

    x=add2hex(lowa,higha)
    y=add2hex(lowb,highb)
    if (len(x)==3) and (len(y)==3)  :
        x, y = x[:2], y[:2]
        midpat = karat416(x,y)
        midx = ((add2hex(x,y)))
        midh = add2hex( midx, midpat[2:])
        mid = []
        # mid = add2hex((midpat[:2] + midh),(4*['00']+['01']) )
        mid = midpat[:2] + midh[:2] + add2hex(midh[2:],(['01']))

    elif (len(x) ==3) and (len(y) == 2) :
        x = x[:2]
        midpat = karat416(x,y)
        midpart = karat416( (add2hex(x, ['01'])), (y))
        midx = ((sub2hex(midpart, midpat)))
        midh = add2hex( midx, midpat[2:])
        mid = []
        mid = midpat[:2] + midh

    elif  (len(y) ==3) & (len(x) == 2):
        y=y[:2]
        midpat = karat416(x,y)
        midpart = karat416( (add2hex(y, ['01'])), (x))
        midx = ((sub2hex(midpart, midpat)))
        midh = add2hex( midx, midpat[2:])
        mid = []
        mid = midpat[:2] + midh
    else :
        mid = karat416(x,y)
    mid0= sub2hex(sub2hex(mid,(r32low)), (r32high))
    mid1 = add2hex(mid0,r32low[2:])
    result432+=(mid1[:2])
    result432 +=(add2hex(mid1[2:],r32high))
    
    return result432[:8]


# a= ['de','9b','57','21']
# b = ['de','9b','57','90']
# print(karat432(b,a))

# f= ['34', '12', '34', '12']
# g= ['f1', '45', '45', 'ff']
# # print(karat432(g,f)) #['f4', '26', 'f1', 'df', '23', 'cb', '26', '12']
# b =(karat432(g,f))

# f= ['1']
# g= [ '1']              #working
# print(karat432(f,g))

# f=['a1', '67', 'eb', 'c8']
# g=['1d', '7e', '92', 'a7']
# # print(karat432(f,g))
# b =(karat432(g,f))


# g= ['34', '12', '34', '12']
# f= ['34', '12', '34', '12']
# b =(karat432(f,g))

# a=(into8(hex(from8(f) * from8(g))[2:]))
# if a==b:
#     print("crct")
# else:
#     print('wrong')
#     print(a)
#     print(b)
