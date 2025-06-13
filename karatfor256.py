from bitstohex import from8 
from add2hex import add2hex
from split import split
from karatfor128 import karatfor128
from sub2hex import sub2hex
from into8bits import into8

def karatfor256(I, J): 

    result4256 = []
    if len(I) <=32 :
        I = I+ (32-len(I))*['00']       
    if len(J) <=32 :
        J = J+ (32-len(J))*['00']
    
    lowi = split(I)[0]   
    lowj = split(J)[0]   
    print(lowi)
    print(lowj)
    r256low = karatfor128(lowi, lowj)
    rm256low = (str(hex((from8(lowi)) * (from8(lowj))))[2:])
    m256low = into8(rm256low)
    print(r256low)
    print(m256low)
    if r256low == m256low :
         print("good with r256 low")
    else:
         print("failed with r256 low k128 ")

    result4256+=(r256low[:16])                                                                                                        
    
    highi = split(I)[1]  
    highj = split(J)[1]  
    r256high = karatfor128(highi, highj)
    
    x=add2hex(lowi,highi)  
    y=add2hex(lowj,highj)
    
    if (len(x) ==17) & (len(y) == 17) : 
        x, y = x[:16], y[:16]                                                           
        midpat = karatfor128(x,y)                                       
        midpart = karatfor128( (add2hex(x, ['01'])), (add2hex(y, ['01'])))     
        midm = sub2hex((sub2hex(midpart, midpat)),['01'])   
        midh = add2hex( midm, midpat[16:])    
        mid = []
        mid = add2hex((midpat[:16] + midh),(32*['00']+['01']) )  

    elif (len(x) ==16) & (len(y) == 17) :
            y = y[:16]  
            midpat = karatfor128(x,y)                
            midpart = karatfor128( (add2hex(y, ['01'])), (x)) 
            midm =((sub2hex(midpart, midpat))) 
            midh = add2hex( midm, midpart[16:])  
            mid = []
            mid = (midpat[:16] + midh) 

    elif (len(y) ==16) & (len(x) == 17) :
            x = x[:16]  
            midpat = karatfor128(x,y)
            midpart = karatfor128( (add2hex(x, ['01'])), (y)) 
            midm =((sub2hex(midpart, midpat))) 
            midh = add2hex( midm, midpart[16:])  
            mid = []
            mid = (midpat[:16] + midh)       
    else:
        mid = karatfor128(x,y)  

    r256mid = mid
    rm256mid = (str(hex((from8(x)) * (from8(y))))[2:])
    m256mid = into8(rm256mid)
    print(r256mid)
    print(m256mid)
    if r256mid == m256mid :
         print("good with r256 mid")
    else:
         print("failed with r256 mid ")
                                                            
    mid0= (sub2hex(mid,(r256low)))
    mid0=   (sub2hex(mid0,(r256high))  )
    mid1 = add2hex(mid0,r256low[16:])   
    result4256 +=(mid1[:16])
    result4256 +=(add2hex(mid1[16:],r256high)) 

    # print(r256low)
    # print(r256high)
    return result4256




p=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']
o=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']
# # o=['1']
print(karatfor256(p,o))

# f= ['1']
# g= [ '1']              #working
# print(karatfor256(f,g))

# A7927E1DD9AB6F50E3D742B6B1C8A73D 94AFBE67AC1F0E1B7DA2956F1C2E43B2
# f=['b2', '43', '2e', '1c', '6f', '95', 'a2', '7d', '1b', '0e', '1f', 'ac', '67', 'be', 'af', '94',
#     '3d', 'a7', 'c8', 'b1', 'b6', '42', 'd7', 'e3', '50', '6f', 'ab', 'd9', '1d', '7e', '92', 'a7']
# # C8EB67A13D9E2C147F03CBE5D7A2F19E 76B0D9FAE31E84CB9F45E7AD13AC90B7
# g=['b7', '90', 'ac', '13', 'ad', 'e7', '45', '9f', 'cb', '84', '1e', 'e3', 'fa', 'd9', 'b0', '76',
#     '9e', 'f1', 'a2', 'd7', 'e5', 'cb', '03', '7f', '14', '2c', '9e', '3d', 'a1', '67', 'eb', 'c8']
# # print((karatfor256(f,g)))
# x =(karatfor256(f,g))

# a=str(hex(0xC8EB67A13D9E2C147F03CBE5D7A2F19E76B0D9FAE31E84CB9F45E7AD13AC90B7 * 0xA7927E1DD9AB6F50E3D742B6B1C8A73D94AFBE67AC1F0E1B7DA2956F1C2E43B2))
# input = a[2:]
# output = into8(input)
# # print(output)

# if x== output:
#      print("good for 256")
# else:
#      print("very bad with 256")