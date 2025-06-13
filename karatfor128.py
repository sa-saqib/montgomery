from into8bits import into8
from add2hex import add2hex
from split import split
from karatfor64 import karatfor64
from sub2hex import sub2hex
from bitstohex import from8

def karatfor128(G, H): 

    result4128 = []
    # if ((E==['00','00','00','00','00','00','00','00']) | (F ==['00','00','00','00','00','00','00','00'])):
    #      result464= ['00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00'] 
    if len(G) <16 :
        G = G+ (16-len(G))*['00']       
    if len(H) <16 :
        H = H+ (16-len(H))*['00']
    
    lowg = split(G)[0]   
    lowh = split(H)[0]   
    r128low = karatfor64(lowg, lowh)
    # a= from8(lowg)
    # b= from8(lowh)
    # c= into8(hex(a * b)[2:])
    # print(f'm128low: {c}')
    # print(f' r128low: {r128low}')
    # if r128low == c:
    #      print('good with r128low')
    # else:
    #      print('failed with r128 low')
    result4128+=(r128low[:8])                                                                                                        
    
    highg = split(G)[1]  
    highh = split(H)[1] 
    r128high = karatfor64(highg, highh)
    # a= from8(highg)
    # b= from8(highh)
    # m128high= into8(hex(a * b)[2:])
    # print(f'm128high: {m128high}')
    # print(f' r128high: {r128high}')
    # if r128low == c:
    #      print('good with r128high')
    # else:
    #      print('failed with r128 high')
    
    
    x=add2hex(lowg,highg)  
    y=add2hex(lowh,highh)
    

    if ((len(x) == 9) and (len(y)) == 9) : 
        x, y = x[:8], y[:8]                                                        
        midpat = karatfor64(x,y) 
        # print(f'x : {x}')
        # print(f'y : {y}')
        # a= from8(x)
        # b= from8(y)
        # mmidpat= into8(hex(a * b)[2:])
        # print(f'mmidpat: {mmidpat}')
        # print(f' midpat: {midpat}')
        # if midpat == mmidpat:
        #     print('good with midpat')
        # else:
        #     print('failed with midpat ')                                 
        midpart = karatfor64( (add2hex(x, ['01'])), (add2hex(y, ['01'])) )         
        midm = sub2hex((sub2hex(midpart, midpat)),['01'])          
        midh = add2hex( midm, midpat[8:])          
        mid = []
        mid = add2hex((midpat[:8] + midh),(16*['00']+['01']) )  

    elif (len(x) ==8) and (len(y) == 9) :
        
            y = y[:8]  
            midpat = karatfor64(x,y)                
            midpart = karatfor64( (add2hex(y, ['01'])), (x))              
            midm =(sub2hex(midpart, midpat))            
            midh = add2hex( midm, midpart[8:])              
            mid = []
            mid = (midpat[:8] + midh) 
               

    elif (len(y) ==8) & (len(x) == 9) :
        
            x = x[:8]  
            midpat = karatfor64(x,y)               
            midpart = karatfor64( (add2hex(x, ['01'])), (y))             
            midm =(sub2hex(midpart, midpat))            
            midh = add2hex( midm, midpart[8:])  
            mid = []
            mid = (midpat[:8] + midh) 
            
       
    else:
        mid = karatfor64(x,y)  
                                                            
    mid0=  sub2hex(mid,r128low)
    mid0=  sub2hex(mid0,r128high)
    mid1 = add2hex(mid0,r128low[8:])
    result4128 +=(mid1[:8])
    result4128 +=(add2hex(mid1[8:],r128high)) 
     
    # print(r128low)
    # print(r128high)
    # print(x)
    # print(y)
    # print(midm)
    # print(mid)
    # print(mid0) ['73', 'bb', 'b9', 'f5', 'ff', '5f', '13', '7e', 'e6'(ikkada e5 raavaali), '20', '21', 'b5', 'd1', '7c', 'c1', '96', '00', '00', '00', '00', '00', '00', '00', '00']
    # print(mid1)
    return result4128

# o=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']
# p=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']
# print(karatfor128(p,o))

# o=['00','00','00','00','00','00','00','00','ff','ff','ff','ff','ff','ff','ff','ff']
# p=['ff','ff','ff','ff','ff','ff','ff','ff','00','00','00','00','00','00','00','00']
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

# f=['3d', 'a7', 'c8', 'b1', 'b6', '42', 'd7', 'e3', '50', '6f', 'ab', 'd9', '1d', '7e', '92', 'a7']
# g= ['9e', 'f1', 'a2', 'd7', 'e5', 'cb', '03', '7f', '14', '2c', '9e', '3d', 'a1', '67', 'eb', 'c8']
# print(karatfor128(f,g))
# ans = ['3e', '84', 'be', 'dc', 'ac', '0d', '59', '80', 'd3', '0f', '8b', 'e4', '54', 'a9', '3d', 'cc', '4e', '3c', '31', 'cd', '4a', '4c', 'e9', 'e7', '8d', '07', '8c', '60', '31', 'b9', 'ef', '44']

f=['b2', '43', '2e', '1c', '6f', '95', 'a2', '7d',
    '1b', '0e', '1f', 'ac', '67', 'be', 'af', '94']
g=['b7', '90', 'ac', '13', 'ad', 'e7', '45', '9f', 'cb', '84', '1e', 'e3', 'fa', 'd9', 'b0', '76']


print(f' result: {karatfor128(f,g)}')
print(['3e', '84', 'be', 'dc', 'ac', '0d', '59', '80', 'd3', '0f', '8b', 'e4', '54', 'a9', '3d', 'cc', '4e', '3c', '31', 'cd', '4a', '4c', 'e9', 'e7', '8d', '07', '8c', '60', '31', 'b9', 'ef', '44'])
# if (karatfor128(f,g) == ans):
#      print('pass')
# else:
#      print('fail')
     
#'3e', '84', 'be', 'dc', 'ac', '0d', '59', '80', 'd3', '0f', '8b', 'e4', '54', 'a9', '3d', 'cc',
#  '4e', '3c', '31', 'cd', '4a', '4c', 'e9', 'e7', '8d', '07', '8c', '60', '31', 'b9', 'ef', '44']


# '3e', '84', 'be', 'dc', 'ac', '0d', '59', '80', 'd3', '0f', '8b', 'e4', '54', 'a9', '3d', 'cc', '4f', '3c', '31', 'cd', '4a', '4c', 'e9', 'e7', '8d', '07', '8c', '60', '31', 'b9', 'ef', '44']
