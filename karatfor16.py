from into8bits import into8
from add2hex import add2hex
from sub2hex import sub2hex
def karatfor16(A,B):   
    if len(A) <2 :
        A= A+ (2-len(A))*['00']       
    if len(B) <2 :
        B = B+ (2-len(B))*['00']

    a= [int(x,16) for x in A]    
    b= [int(x,16) for x in B]
    result = []

    low = into8(str(hex(a[0]*b[0]))[2:])  
    if len(low)<2 :
        low+= ["00"] * (2 -(len(low)))
    
    result.append(low[0])
    high = into8(str(hex(b[1]*a[1]))[2:])        
    
    A2h= into8(str(hex(a[0]+a[1]))[2:])           
    B2h= into8(str(hex(b[0]+b[1]))[2:])           
    if (len(A2h)) | (len(B2h)) == 2 : 
        c= karatfor16(A2h, B2h)                          
    else:
        c= into8(str(hex((a[0] + a[1]) * (b[0] + b[1])))[2:])   
                                              
    mid = sub2hex(sub2hex(c,(low)), (high))    
   
    mid0 = add2hex(mid,[low[1]])               
    result.append(mid0[0])                     
    mid0 = mid0[1:]               
    result=result+(add2hex(mid0,high))        
    
    if len(result)<4 :
        result+= ["00"] * (4 -(len(result)))

    return result[:4]

# x = ['0','01'] 
# y = ['01','0']
# print(karatfor16(x, y))

# # if len(result)<4 :
# #     result+= ["00"] * (4 -(len(result)))
# print("hello ",result)

# x = [] 
# y = ['f', 'f']
# result = karatfor16(x, y)
# if len(result)<4 :
#     result+= ["00"] * (4 -(len(result)))
# print("hello ",result)
     
'''mid00 = f"{mid0 & 0xff:02x}"
   
        result.append(mid00)
    #mid1 = ((mid & 0xff00)>>8)
    #mid1 = ((mid & ((1<<8)-1))>>8)
        mid1 = (str(hex(mid0)[2:-2] ))
   
   
        highf =hex(int( mid1,16)+ high)
   
   
        result.append(str(highf[4:]))
        result.append(str(highf[2:4]))
   
   
    #result = str(highf) + str(mid00) + str(low0)
    return result'''


        
'''
        mid0 = mid + ((low & 0xff00)>>8)
   
     
        mid00 = f"{mid0 & 0xff:02x}" 
   
        result.append(mid00)
    #mid1 = ((mid & 0xff00)>>8)
    #mid1 = ((mid & ((1<<8)-1))>>8)
        mid1 = (str(hex(mid0)[2:-2] ))

    
        highf =hex(int( mid1,16)+ high)
   
    
        result.append(str(highf[4:]))
        result.append(str(highf[2:4]))
    
    
    #result = str(highf) + str(mid00) + str(low0)'''
        
    


    


 




 