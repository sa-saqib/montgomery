#!/usr/bin/env python3
'''
import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))


#----------------------------------------------------------------------------------------------------------------------

m=  [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for i in range (len(m)):
    print(chr(m[i]),end ="")
# for ASCII to ordinal chr() , for ordinal to ASCII ord()
#----------------------------------------------------------------------------------------------

a= '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
k=bytes.fromhex(a)
print(k)

#----------------------------------------------------------------------------------------

import base64 
a= "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte = bytes.fromhex(a)
print(byte)

b= base64.b64encode(byte).decode('utf-8')
print(b)

#----------------------------------------------------------------------------------------------------------------------------------

from Crypto.Util.number import *
b = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes = long_to_bytes(b)
print(bytes)

#----------------------------------------------------------------------------------------------------------------------------------

l= 'label'
list =[]
newlist=[]
for i in range (len(l)):
    list.append(ord(l[i]))

for i in list:
    newlist.append(i ^ 13)

for i in range (len(newlist)):
    print(chr(newlist[i]),end ="")

#--------------------------------------------------------------------------------------------------------------------

KEY1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2KEY1 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e

KEY2KEY3 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 
FLAGKEY1KEY3KEY2 = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
flag = hex(FLAGKEY1KEY3KEY2 ^ KEY2KEY3 ^ KEY1)
falg2 =( (flag[2::]))

flagbyte  = bytes.fromhex(falg2)
print(flagbyte)

flagans= base64.b64encode(flagbyte).decode('utf-8')
print(flagans)

from pwn import xor
k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print(xor(k1,k2_3,flag)) 

#--------------------------------------------------------------------------------------------------

from pwn import xor
a= '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
bytexor = bytes.fromhex(a)
print(bytexor)
c= "7fk h! O!%O}iOv$f eb!'#Ori'um"
cis= bytes.fromhex(c)
result = xor(bytexor, cis)


'''