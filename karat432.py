
from add2hex import add2hex
from split import split
from karat416 import karat416
from sub2hex import sub2hex
def karat432(C, D): 
    if len(C) <4 :
        C = C+ (4-len(C))*['00']       
    if len(D) <4 :
        D = D+ (4-len(D))*['00']

    result432 = []
    lowa=split(C)[0]                                                                 
    lowb = split(D)[0]                                                             
    r32low = karat416(lowa, lowb)                                                  
    result432+=(r32low[:2])                                                                                                         
    
    higha = split(C)[1]  
    highb = split(D)[1]  
    r32high = karat416(higha, highb)                                             

    x=add2hex(lowa,higha)                                                            
    y=add2hex(lowb,highb)                                                            
    
    if (len(x)==3) & (len(y)==3)  : 
        x, y = x[:2], y[:2]                                                           
        midpat = karat416(x,y)                                        
        midpart = karat416( (add2hex(x, ['01'])), (add2hex(y, ['01'])) )       
        midm = sub2hex((sub2hex(midpart, midpat)),['01'])        
        midh = add2hex( midm, midpat[2:])     
        mid = []
        mid = add2hex((midpat[:2] + midh),(4*['00']+['01']) )    

    elif (len(x) ==3) & (len(y) == 2) :
        x = x[:2] 
        midpat = karat416(x,y)     
        midpart = karat416( (add2hex(x, ['01'])), (y))  
        midm = ((sub2hex(midpart, midpat)))
        midh = add2hex( midm, midpat[2:])  
        mid = []
        mid = (midpat[:2] + midh)   

    elif  (len(y) ==3) & (len(x) == 2):
        y=y[:2]
        midpat = karat416(x,y)     
        midpart = karat416( (add2hex(y, ['01'])), (x))         
        midm = ((sub2hex(midpart, midpat)))  
        midh = add2hex( midm, midpat[2:])       
        mid = []
        mid = (midpat[:2] + midh)   
           
    else :
        mid = karat416(x,y)                                                     
    
    mid0= sub2hex(sub2hex(mid,(r32low)), (r32high))                              
    mid1 = add2hex(mid0,r32low[2:])                                                
    result432+=(mid1[:2])
    result432 +=(add2hex(mid1[2:],r32high))   
    # print(midpat) 
    # print(midpart)  
    # print(midm) 
    # print(midh) 
    # print(mid1) 
    # print(mid)
    # print(mid0)
    return result432[:8]   


# a= ['de','9b','57','21']
# b = ['de','9b','57','90']
# print(karat432(b,a))

# g= ['34', '12', '34', '12']
# f= ['f1', '45', '45', 'ff']            
# print(karat432(f,g)) #['f4', '26', 'f1', 'df', '23', 'cb', '26', '12']

# f= ['1']
# g= [ '1']              #working
# print(karat432(f,g))

# f=['a1', '67', 'eb', 'c8']
# g=['1d', '7e', '92', 'a7']
# print(karat432(f,g))