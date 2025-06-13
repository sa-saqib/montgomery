
from add2hex import add2hex
from split import split
from karatfor8 import karatfor8
from sub2hex import sub2hex
def karat416(C, D): 
    if len(C) <2 :
        C = C+ (2-len(C))*['00']       
    if len(D) <2 :
        D = D+ (2-len(D))*['00']

    result416 = []
    lowa=split(C)[0]                                                                 
    lowb = split(D)[0]                                                             
    
    r16low = karatfor8(lowa, lowb)                                                  

    result416+=(r16low[:1])                                                                                                         
    
    higha = split(C)[1]  
    highb = split(D)[1]  
    r16high = karatfor8(higha, highb)                                             

    x=add2hex(lowa,higha)                                                            
    y=add2hex(lowb,highb)                                                            
    
    if (len(x)==2) & (len(y)==2)  : 
        x, y = x[:1], y[:1]                                                           
        midpat = karatfor8(x,y)                                        
        midpart = karatfor8( (add2hex(x, ['01'])), (add2hex(y, ['01'])) )       
        midm = sub2hex((sub2hex(midpart, midpat)),['01'])        
        midh = add2hex( midm, midpat[1:])     
        mid = []
        mid = add2hex((midpat[:1] + midh),(2*['00']+['01']) )    

    elif (len(x) ==2) & (len(y) == 1) :
        x = x[:1] 
        midpat = karatfor8(x,y)     
        # midpart = karatfor8( (add2hex(x, ['01'])), (y))  
        # midm = ((sub2hex(midpart, midpat)))
        # midh = add2hex( midm, midpart[1:])  
        # mid = []
        # mid = midpat[:1] + midh 
        mid = midpat[:1] + add2hex(midpat[1:],y)
            # print(mid)

    elif  (len(y) ==2) & (len(x) == 1):
        
        y=y[:1]
        midpat = karatfor8(x,y)
            # print(midpat)       
        # midpart = karatfor16( (add2hex(y, ['01'])), (x))  
        #     # print(midpart)        
        # midm = ((sub2hex(midpart, midpat)))  
        #     # print(midm) 
        # midh = add2hex( midm, midpart[2:])       
        # mid = []
        # mid = midpat[:2] + midh  
        mid = midpat[:1] + add2hex(midpat[1:],x)
            # print(mid) 

               
    else :
        mid = karatfor8(x,y)                                                     
    
    mid0= sub2hex(sub2hex(mid,(r16low)), (r16high))                              
    mid1 = add2hex(mid0,r16low[1:])                                                
    result416+=(mid1[:1])
    result416 +=(add2hex(mid1[1:],r16high))   


    return result416[:4]                                         

# g= ['f2','f3']
# f= ['2f', '1f']            #working
# print(karat416(f,g))

# f= ['f2','f3']
# g= ['ff', 'f4']            #working
# print(karat416(g,f))

# f= ['ff','ff']
# g= ['ff', 'ff']            #working
# print(karat416(f,g))

# f= ['92','53']
# g= ['2f', '1f']              #working
# print(karat416(f,g))

# f= ['1']
# g= [ '1']              #working
# print(karat416(f,g))
