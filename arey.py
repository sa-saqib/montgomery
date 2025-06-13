'''a= [ 0,0,1,0,2,3,0,5,0,8,0,0,0,0,9,0,0,10,0,0,0,0]
for i in a:
    if i ==0:
        a.remove(i)
        a.append(i)  
print(a)'''

def karatfor16(a, b):
    low = (a[0]) * (b[0])  
         
    low0 = f"{low & 0xff:02x}"      
    low1 = ((low & 0xff00)>>8)
     

    

    high = (a[1] * b[1])
      

   
    mid = (a[0] + a[1]) * (b[0] + b[1]) - (low)- (high)
    
    mid0 = mid + ((low & 0xff00)>>8)
    print(hex(mid0))
    mid00 = f"{mid0 & 0xff:02x}"
    print(mid00)
    #mid1 = ((mid & 0xff00)>>8)
    #mid1 = ((mid & ((1<<8)-1))>>8)
    mid1 = (str(hex(mid0)[2:-2] ))
    print(mid1)
 
    highf =hex(int( mid1,16)+ high)
    print((highf))
 
    result = str(highf) + str(mid00) + str(low0)
    return result
 
#x = [0xfe, 0xf1]
#y = [0xda, 0xda]
#print(karatfor16(x, y))




