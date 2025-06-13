#r^2 mod n for 256(R22) =0x4fffffffdfffffffffffffffefffffffbffffffff0000000000000003 (227 bits)
# N ^-1 =  0xfffffffdfffffffffffffffffffffffeffffffffffffffffffffffff (224 bits)

# r^2 mod n for 384(R23)= 0x10000000200000000fffffffe000000000000000200000000fffffffe00000001 (257 bits)
# N ^-1 = -0x14000000140000000c00000002fffffffcfffffffafffffffbfffffffe00000000000000010000000100000001 (357 bits)

# r^2 mod n for 521  = 1
# N^-1 = -1
from karatfor256 import karatfor256
from karatfor384 import karatfor384
from karatfor528 import karatfor528

from mod import mod
from add2hex import add2hex
from righ8shift import ri8s 

# from mulwithinv import mulwinv
# from mulxr2 import mulwithr2

# jot down all the info required like for x . r2 mod N 
def redc(v,curve):  # { v+ [ ( v *(- n^-1) mod R) N ] } / R
    result =[]
    N =[['ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', '00', '00','00', '00',
        '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', 'ff', 'ff', 'ff', 'ff'],
        
        ['ff', 'ff', 'ff', 'ff', '00', '00', '00', '00', '00', '00', '00', '00', 'ff', 'ff', 'ff', 'ff', 
         'fe', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff','ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 
         'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff'],

        ['ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 
          'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 
          'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 
          'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', '01']
          ]
    # nlen = [ 32, 48, 66]
     #(the below is -N_inv which we could directly use and do the addition instead of subtraction )      
    N_inv = [['01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', 
              '00', '00', '00', '00', '00', '00', '00', '00', '02', '00', '00', '00', 'ff', 'ff', 'ff', 'ff'],

              ['01', '00', '00', '00', '01', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', 'fe',
                'ff', 'ff', 'ff', 'fb', 'ff', 'ff', 'ff', 'fa', 'ff', 'ff', 'ff', 'fc', 'ff', 'ff', 'ff', '02', '00',
                '00', '00', '0c', '00', '00', '00', '14', '00', '00', '00', '14', '00', '00', '00'] 
              ]
    if curve ==0:
        m= karatfor256(v[:32],N_inv[0])
        inner = mod(m,0) #inner = m[:32]
        right = karatfor256(inner,N[0])
        num = add2hex(v,right)  
        result = ri8s(num,256)


    elif curve ==1:
        m= karatfor384(v[:48],N_inv[1])
        inner = mod(m,0) #inner = m[:48]
        right = karatfor384(inner,N[1])
        num = add2hex(v,right)  
        result = ri8s(num,384)

    elif curve ==2:
        # m = v
        inner = mod(v,2) 
        right = karatfor528(inner,N[2])
        num = add2hex(v,right)  
        result = ri8s(num,521)
    
    return result

    # la = len(a)
    # lb = len(b)
    # ln = len(N[1])
    # while la>ln:     #sochneki baat hai agar a is 1024/512 bits and n is p256
    #     diff = la - ln
    #     if diff ==1 :
    #         while a_greaterthanb(a,N):
    #             a = sub2hex(a,N)
    #     elif diff >1:
    #         a = sub2hex(a, ((N-1) * ['00']) + N  )
    #         while a_greaterthanb(a,N):
    #             a = sub2hex(a,N)

    # while lb>ln:     #sochneki baat hai agar a is 1024/512 bits and n is p256
    #     dif = lb - ln
    #     if dif ==1 :
    #         while a_greaterthanb(b,N):
    #             b = sub2hex(b,N)
    #     elif dif >1:
    #         b = sub2hex(b, ((N-1) * ['00']) + N  )
    #         while a_greaterthanb(b,N):
    #             b = sub2hex(b,N)












    
    




