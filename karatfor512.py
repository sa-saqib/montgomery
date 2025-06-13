from add2hex import add2hex
from split import split
from karatfor256 import karatfor256
from sub2hex import sub2hex

def karatfor512(k,l): 
    if len(k) <= 64:
        k= k + ((64-len(k))*['00'])
    if len(l) <= 64:
        l= l + ((64-len(k))*['00']  )   

    result4512 = []  
        
    lowk = split(k)[0]   
    lowl = split(l)[0]   
    r512low = karatfor256(lowk, lowl) 

    result4512+=(r512low[:32])                                                                                                        
    
    highk = split(k)[1]
      
    highl = split(l)[1]  
    
    r512high = karatfor256(highk, highl)
    
    
    x=add2hex(lowk,highk)  
    y=add2hex(lowl,highl)
    

    if ((len(x)) & (len(y)) == 33) : 
        x, y = x[:32], y[:32]                                                          
        
        midpat = karatfor256(x,y)                                       
        
       
        midpart = karatfor256( (add2hex(x, ['01'])), (add2hex(y, ['01'])) ) 
        
        midm = sub2hex((sub2hex(midpart, midpat)),['01'])  
        
        midh = add2hex( midm, midpat[32:])  
        
        mid = []
        mid = add2hex((midpat[:32] + midh),(64*['00']+['01']) )  

    elif (len(x) ==32) & (len(y) == 33) :
        if x==['00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00'] :
            mid =['00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00']
        else:
            y = y[:32]  
            midpat = karatfor256(x,y)
                
            midpart = karatfor256( (add2hex(y, ['01'])), (x))  
            

            midm =sub2hex((sub2hex(midpart, midpat)),['01']) 
            

            midh = add2hex( midm, midpart[32:])  
            
            mid = []
            mid = (midpat[:32] + midh) 
               

    elif (len(y) ==32) & (len(x) == 33) :
        if y==['00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00'] :
            mid =['00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00']
        else:
            x = x[:32]  
            midpat = karatfor256(x,y)
               
            midpart = karatfor256( (add2hex(x, ['01'])), (y))  
           

            midm =sub2hex((sub2hex(midpart, midpat)),['01']) 
            

            midh = add2hex( midm, midpart[32:])  
           
            mid = []
            mid = (midpat[:32] + midh) 
            
       
    else:
        mid = karatfor256(x,y)  
                                                            
    mid0= (sub2hex(mid,(r512low))) 
     
    
    mid0=   (sub2hex(mid0,(r512high))  )
                          
    mid1 = add2hex(mid0,r512low[32:])                                         
       
    result4512 +=(mid1[:32])
    result4512 +=(add2hex(mid1[32:],r512high)) 
     

    return result4512


zi= ['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']

yes=['ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff','ff']
print(karatfor512(zi,yes))