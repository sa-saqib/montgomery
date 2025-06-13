from add2hex import add2hex
from split import split
from karat432 import karat432
from sub2hex import sub2hex
from bitstohex import from8
from into8bits import into8

def karatfor64(E, F): 
                      
    result464 = []
    # if ((E==['00','00','00','00','00','00','00','00']) | (F ==['00','00','00','00','00','00','00','00'])):
    #      result464= ['00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00'] 
    if len(E) <8 :
        E = E+ (8-len(E))*['00']       
    if len(F) <8 :
        F = F+ (8-len(F))*['00']
    
    lowe = split(E)[0]   
    lowf = split(F)[0]   
    r64low = karat432(lowe, lowf)
    a= from8(lowe)
    b= from8(lowf)
    m64low= into8(hex(a * b)[2:])
    print(f'm64low: {m64low}')
    print(f' r64low: {r64low}')
    if r64low == m64low:
         print('good with r64low')
    else:
         print('failed with r64 low')
    result464+=(r64low[:4])                                                                                                        
    
    highe = split(E)[1] 
    highf = split(F)[1]  
    r64high = karat432(highe, highf)
    a= from8(highe)
    b= from8(highf)
    m64high= into8(hex(a * b)[2:])
    print(f'm64high: {m64high}')
    print(f' r64high: {r64high}')
    if r64high == m64high:
         print('good with r64high')
    else:
         print('failed with r64 high')
    
    x=add2hex(lowe,highe)  
    y=add2hex(lowf,highf)
    print(f'x: {x}')
    print(f' y: {y}')

   
    if (len(x)) & (len(y)) == 5 : 
        x, y = x[:4], y[:4]                                                       
        print(x,y)
        midpat = karat432(x,y)
        a= from8(highe)
        b= from8(highf)
        mmidpat= into8(hex(a * b)[2:])
        print(f'mmidpat: {mmidpat}')
        print(f' midpat: {midpat}')
        if midpat == mmidpat:
            print('good with midpat')
        else:
            print('failed with midpat')                                   
       
        midpart = karat432( (add2hex(x, ['01'])), (add2hex(y, ['01'])) ) 
        
        midm = sub2hex((sub2hex(midpart, midpat)),['01'])  
        
        midh = add2hex( midm, midpat[4:]) 
        
        mid = []
        mid = add2hex(((midpat[:4] + midh)),(8*['00']+['01']) )
        

    elif (len(x) ==4) & (len(y) == 5) :
        
            y = y[:4]  
            midpat = karat432(x,y)
            a= from8(x)
            b= from8(y)
            mmidpat= into8(hex(a * b)[2:])
            print(f'mmidpat: {mmidpat}')
            print(f' midpat: {midpat}')
            if midpat == mmidpat:
                print('good with midpat')
            else:
                print('failed with midpat')

            midpart = karat432( (add2hex(y, ['01'])), (x))  
            c= b +1
            d= a
            mmidpart= into8(hex(c * d)[2:])
            print(f'mmidpart: {mmidpart}')
            print(f' midpart: {midpart}')
            if midpart == mmidpart:
                print('good with midpart')
            else:
                print('failed with midpart') 
            
            # midm =((sub2hex(sub2hex(midpart, midpat)),['01'])  ) 
            midm = ((sub2hex(midpart, midpat)))
            s= from8(midpart)
            t= from8(midpat)
            q= into8(hex( s - t)[2:])
            print(f'mmidm: {q}')
            print(f' midm: {midm}')
            if midm == q:
                print('good with midm')
            else:
                print('failed with midm') 

            midh = add2hex( midm, midpart[4:])  
            s= from8(midpart[4:])
            t= from8(midm)
            q= into8(hex( s + t)[2:])
            print(f'mmidh: {q}')
            print(f' midh: {midh}')
            if midh == q:
                print('good with midh')
            else:
                print('failed with midh') 
            
            mid = []
            mid = (midpat[:4] + midh) 
            

            
            
    elif (len(y) ==4) & (len(x) == 5) :
        
            x = x[:4] 
            midpat = karat432(x,y)
            print(x,y)
            midpat = karat432(x,y)
            a= from8(highe)
            b= from8(highf)
            mmidpat= into8(hex(a * b)[2:])
            print(f'mmidpat: {mmidpat}')
            print(f' midpat: {midpat}')
            if midpat == mmidpat:
                print('good with midpat')
            else:
                print('failed with midpat')
               
            midpart = karat432( (add2hex(x, ['01'])), (y))   
            
            midm =((sub2hex(midpart, midpat)))
            
            midh = add2hex( midm, midpart[4:])  
           
            mid = []
            mid = (midpat[:4] + midh) 
               

       
    else:
        
            mid = karat432(x,y)  


    g= from8(x)
    h = from8(y)
    i = into8(hex(g *h)[2:])
    print(f'i: {i}')
    print(f' mid: {mid}')
    if mid == i:
        print('good with mid')
    else:
        print('failed with mid')

    mid0= (sub2hex(mid,(r64low))) 
    
    mid0=   (sub2hex(mid0,(r64high))  )
                         
    mid1 = add2hex(mid0,r64low[4:])                                         
      
    result464 +=(mid1[:4])
    result464 +=(add2hex(mid1[4:],r64high)) 
    
    # print(midpat)
    # print(midpart)
    # print(midm)
    # print(midh)
    # print(mid)
    return result464[:16] 

x = ['cd', '51', '4d', 'c8', 'd6', '53', '52', '12']
y = ['82', '15', 'cb', 'f6', 'a7', 'c1', 'f6', '15']
print(karatfor64(x,y)) 

# o=['ef','cd','ab','90','78','56','34','12']
# p=['ef','cd','ab','90','78','56','34','12']
# print(karatfor64(o,p))  #0x14b66dc328828bca6475f09a2f2a521

# o= ['78','56','34','12','78','56','34','12']
# p =['78','56','34','12','78','56','34','12']
# print(karatfor64(o,p)) 


# o=['ff','ff','ff','ff','ff','ff','ff','ff'] # 01 +7(00)+ fe + 7(ff)
# p=['ff','ff','ff','ff','ff','ff','ff','ff']
# print(karatfor64(o,p))   #ffff ffff ffff fffe 0000 0000 0000 0001

# o=['00','00','00','00','ff','ff','ff','ff']
# p=['ff','ff','ff','ff','00','00','00','00']
# print(karatfor64(p,o))   #0xffff fffe 0000 0001 0000 0000

# p=['1']
# o=['ff','ff','ff','ff','ff','ff','ff','ff']
# print(karatfor64(o,p))

# o=['ef','cd','ab','90','ef','cd','ab','90']
# p=['ef','cd','ab','90','ef','cd','ab','ff']
# print(karatfor64(p,o))

# f= ['1']
# g= [ '1']              #working
# print(karatfor64(f,g))

# f=['b2', '43', '2e', '1c', '6f', '95', 'a2', '7d']
# g= ['b7', '90', 'ac', '13', 'ad', 'e7', '45', '9f']
# print(karatfor64(f,g))

# f=['1b', '0e', '1f', 'ac', '67', 'be', 'af', '94']
# g=['cb', '84', '1e', 'e3', 'fa', 'd9', 'b0', '76']
# print(karatfor64(f,g))