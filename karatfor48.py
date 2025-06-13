from add2hex import add2hex
from karatfor16 import karatfor16
from karatfor32 import karatfor32
from sub2hex import sub2hex
def karatfor48(O, P): 

    result448 = []
    lowa=O[:4]                                                   
    lowb = P[:4]                                                             
    
    r48low = karatfor32(lowa, lowb) 
                                                    
    result448+=(r48low[:4])                                                                                                     
    
    higha =  O[4:]
    highb =  P[4:]    
    r48high = karatfor16(higha, highb) 
    
    x=add2hex(lowa,higha)                                                           
    y=add2hex(lowb,highb)                                                            
    
    if (len(x)==5) & (len(y)==5)  : 
        x, y = x[:2], y[:2]                                                          
        midpat = karatfor16(x,y)                                     
        midpart = karatfor16( (add2hex(x, ['01'])), (add2hex(y, ['01'])) )      
        midm = sub2hex((sub2hex(midpart, midpat)),['01'])   
        # print(midm)     
        # midh = add2hex( midm, midpat[2:]) 
        # print(midh)     
        mid = []
        mid = midpat +  midm + ['01'] 

    elif (len(x) ==5) & (len(y) == 4) :
        if y==['00','00','00','00'] :
            mid =['00','00','00','00','00','00','00','00']
        else:
            x = x[:4]  
            midpat = karatfor32(x,y)     
            midpart = karatfor32( (add2hex(x, ['01'])), (y))  
            midm = sub2hex((sub2hex(midpart, midpat)),['01'])  
            midh = add2hex( midm, midpart[4:])  
            mid = []
            mid = midpat[:4] + midh 
            # print(mid)

        

    elif  (len(y) ==5) & (len(x) == 4):
        if x==['00','00','00','00'] :
            mid =['00','00','00','00','00','00','00','00']
        else:
            y=y[:4]
            midpat = karatfor32(x,y)       
            midpart = karatfor32( (add2hex(y, ['01'])), (x))         
            midm = sub2hex((sub2hex(midpart, midpat)),['01'])        
            midh = add2hex( midm, midpart[4:])       
            mid = []
            mid = midpat[:4] + midh       
                 
    else :
        if (x == ['00','00','00','00']) | (y==['00','00','00','00']):
            mid =['00','00','00','00','00','00','00','00']
        else:
            mid = karatfor32(x,y)                                                       #[80,01,98,18]
    
    mid0= sub2hex(sub2hex(mid,(r48low)), (r48high))                                 #[c0,00,4c,0c] 
    mid1 = add2hex(mid0,r48low[4:])                                                 #[e6,06,4c,0c]
    result448+=(mid1[:4])
    result448 +=(add2hex(mid1[4:],r48high))                                         #60 ,00 e6, 06, ac, 0c, 26, 06
    return result448[:12]                                         

# g= ['ff','ff','ff','ff','ff','ff']
# f= ['34','12','34','12','34','12']          
# print(karatfor48(f,g))  #0x1234 1234 1233 edcb edcb edcc

# f= ['ff','ff','ff','ff','ff','ff']
# g= ['ff','ff','ff','ff','ff','ff']          
# print(karatfor48(f,g))    #0xfffffffffffe000000000001

# f= ['34','12','34','12','34','12']
# g= ['34','12','34','12','34','12']          
# print(karatfor48(f,g))



