from add2hex import add2hex
from split import split
from karat416 import karat416
from sub2hex import sub2hex
def karatfor32(C, D): #x = [0x32, 0x34, 0xfe, 0xf1] f1fe 3432                       [34, 12, 34, 12]
                      #y = [0xba,0xba,0xda, 0xda]  dada baba                        [78 ,56, 78, 56]
    #c= [int(x,16) for x in C]    #[50, 52, 254, 241]
    #d= [int(x,16) for x in D]    #[186, 186, 218, 218]
    if len(C) <4 :
        C = C+ (4-len(C))*['00']       
    if len(D) <4 :
        D = D+ (4-len(D))*['00']

    result432 = []
    lowa=split(C)[0]                                                                 #[34, 12]
    lowb = split(D)[0]                                                              #[78 ,56]
    r32low = karat416(lowa, lowb)                                                  #[60,00,26,06]

    result432+=(r32low[:2])                                                          #[60,00]                                                 
    
    higha = split(C)[1]  
    highb = split(D)[1]  
    r32high = karat416(higha, highb)                                               #[60,00,26,06]

    x=add2hex(lowa,higha)                                                            #[68, 24]
    y=add2hex(lowb,highb)                                                         #[f0, ac]
    
    
    if (len(x)==3) & (len(y)==3)  : #1fffe *1fffe  = 3 fff8 0004
        x, y = x[:2], y[:2]                                                           #[fe, ff] 
        midpat = karat416(x,y)                                       #FFFC 0004     #[04, 00, fc, ff]
        midpart = karat416( (add2hex(x, ['01'])), (add2hex(y, ['01'])) ) #FFFE 0001  #[01, 00, fe, ff]      
        midm = sub2hex((sub2hex(midpart, midpat)),['01'])  #1fffd #fffd -1 #1fffc      
        midh = add2hex( midm, midpat[2:])  #1 FFF8     
        mid = []
        mid = add2hex((midpat[:2] + midh),(4*['00']+['01']) )  #04,00,f8,ff  

    elif (len(x) ==3) & (len(y) == 2) :
        x = x[:2]  #fffe
        midpat = karat416(x,y)     
        midpart = karat416( (add2hex(x, ['01'])), (y))  #1650 bf85  
        midm = ((sub2hex(midpart, midpat))) #bbc4 
        midh = add2hex( midm, midpart[2:])  #1650 + bbc4 = d214
        mid = []
        mid = midpat[:2] + midh 
            # print(mid)


    elif  (len(y) ==3) & (len(x) == 2):
        
        y=y[:2]
        midpat = karat416(x,y)
            # print(midpat)       
        midpart = karat416( (add2hex(y, ['01'])), (x))  #1650 bf85 
            # print(midpart)        
        midm = ((sub2hex(midpart, midpat))) #bbc4 
            # print(midm) 

        midh = add2hex( midm, midpart[2:])  #1650 + bbc4 = d214        
        mid = []
        mid = midpat[:2] + midh       
            # print(mid) 

               
    else :
        mid = karat416(x,y)                                                       #[80,01,98,18]
    
    mid0= sub2hex(sub2hex(mid,(r32low)), (r32high))                                 #[c0,00,4c,0c] 
    mid1 = add2hex(mid0,r32low[2:])                                                 #[e6,06,4c,0c]
    result432+=(mid1[:2])
    result432 +=(add2hex(mid1[2:],r32high))  
    

    print(midpat)
    print(midpart)
    print(midm)
    print(midh)
    print(mid)
    return result432[:8]                                         

# a= ['de','9b','57','21']
# b = ['de','9b','57','90']
# print(karatfor32(a,b))


# f= ['34', '12', '34', '12']
# g= ['ff', 'ff', 'ff', 'ff']            #working
# print(karatfor32(f,g))


# g= ['34', '12', '34', '12']
# f= ['78','56', '78','56']            #working
# print(karatfor32(f,g)) #626 0CAC 06E6 0060

# n = ['ff', 'ff', 'ff', 'ff']
# m = ['90','10','ff','ff']
# print(karatfor32(m,n))    #FFFF 108F 0000 EF70

# n= ['00']
# m = ['0']
# print(karatfor32(m,n))      

# n = ['32', '34', 'fe', 'f1']
# m = ['ba','ba','ff','fa']              #working
# print(karatfor32(m,n))     #ED43 FBB1 566C 4054

# n = ['32', '34', 'fe', 'f1']
# m = ['ba','ba','da','da']           #working
# print(karatfor32(m,n))  #CEE1 3B6D 8B32 4054
    
# n = ['ef', 'cd', 'ab', '90']
# m = ['ef', 'cd', 'ab', 'ff']          #working
# print(karatfor32(m,n)) #51C1 BAF9 A2F2 A521

# f= ['34', '12', '34', '12']
# g= ['34', '12', '34', '12']         
# print(karatfor32(f,g))

# g= ['1']
# f= ['ff','ff', 'ff', 'ff']
# print(karatfor32(f,g))

# g= ['34', '12', '34', '12']
# f= ['f1', '45', '45', 'ff']            
# print(karatfor32(f,g)) #1226 CB23 DFF1 26F4
    
'''
    if (len(x)) | (len(y)) == 3:        
        z= karatfor32(x,y)
        
       ''' 
        






'''
    low = (a[0]) * (b[0])
          
    low0 = f"{low & 0xff:02x}"  
   
    result.append(low0)     
    low1 = ((low & 0xff00)>>8)
     
     
    high = (a[1] * b[1])
    
    
    mid = (a[0] + a[1]) * (b[0] + b[1]) - (low)- (high)
    
    mid0 = mid + ((low & 0xff00)>>8)
   
     
    mid00 = f"{mid0 & 0xff:02x}" 
   
    result.append(mid00)
    #mid1 = ((mid & 0xff00)>>8)
    #mid1 = ((mid & ((1<<8)-1))>>8)
    mid1 = (str(hex(mid0)[2:-2] ))
    
    
    highf =hex(int( mid1,16)+ high)
   
    
    result.append(str(highf[4:]))
    result.append(str(highf[2:4]))
    
    
    #result = str(highf) + str(mid00) + str(low0)
    return result'''

 #54 40 12 26
                        #32 8b 6d 3b e1 ce