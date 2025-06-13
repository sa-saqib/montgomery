
# print(hex(0x90abcdef * 0xffabcdef)) #0x907c394443f2a521
# print(hex(0x90abcdef * 0x90abcdef)) #0x51c1baf9a2f2a521
# print(hex(0x21579bde * 0x90579bde)) #0x12ccb0bfcdca9484
# print(hex(0x121579bde * 0x190579bde))  #0x1c47be87bcdca9484
# print(hex(0x90abcdef90abcdef  * 0xffabcdef90abcdef )) #0x907c39452630995f38a7053ba2f2a521
# print(hex(0xf1fe3432 * 0xfaffbaba)) #0xed43fbb1566c4054
# print(hex(0x1234567890abcdef * 0x1234567890abcdef )) #0x14b66dc328828bca6475f09a2f2a521
# print(hex(0x90ffffffffffffffffffabcdef90abcdef* 0xffffffffffffffff90abcdef90abcdef )) 
#0x90ffffffffffffffc0f0fb72a081fb724e00249d6604d8fd8138a7053ba2f2a521
# print(hex(0x90ffffffffffffff  * 0xffffffffffffffff ))
# print(hex(0xffffffff00000000 * 0xffffffff)) #0xfffffffe0000000100000000
# print(hex(0xffffffffffffffff90abcdef90abcdef * 0x90ffffffffffffffffabcdef90abcdef))
# 0x90ffffffffffffffc09d1d94419d1d935f249d6604d8fd8138a7053ba2f2a521
# print(hex(0x19F0C7D3A6B84E1F4DA59CE82A1F3D76C8EB67A13D9E2C147F03CBE5D7A2F19E76B0D9FAE31E84CB9F45E7AD13AC90B7 * 0x7FA3D1C2B8479B6F215D9EA43B6F0C83A7927E1DD9AB6F50E3D742B6B1C8A73D94AFBE67AC1F0E1B7DA2956F1C2E43B2))
# print(hex(0xC8EB67A13D9E2C147F03CBE5D7A2F19E76B0D9FAE31E84CB9F45E7AD13AC90B7 * 0xA7927E1DD9AB6F50E3D742B6B1C8A73D94AFBE67AC1F0E1B7DA2956F1C2E43B2))
from into8bits import into8

# print(hex(0x19F0C7D3A6B84E1F4DA59CE82A1F3D76 * 0x7FA3D1C2B8479B6F215D9EA43B6F0C83))
print(into8(hex((0x76b0d9fae31e84cb9f45e7ad13ac90b7) * (0x94afbe67ac1f0e1b7da2956f1c2e43b2))[2:]))
# print(hex(0x9f45e7ad13ac90b7 * 0x7da2956f1c2e43b2))
# c=((0x76b0d9fae31e84cb * 0x94afbe67ac1f0e1b))
# d= (a - b - c)
# print(hex(d))

# from bitstohex import from8

# mid = from8(['dc', 'd6', 'c9', '0d', '79', '2f', '3b', 'cf', '73', '28', 'ad', '15', '03', '36', 'b1', 'db', '00', '00', '00', '00', '00', '00', '00', '00'])
# mid1 = from8(['69', '1b', '10', '18', '79', 'cf', '27', '51', '8d', '07', '8c', '60', '31', 'b9', 'ef', '44'])

# print(f'ans: {hex(mid - mid1)}')

# def tobinary(a):
#     binary = []
#     b =''
#     for hexstr in a:
        
#         binary_str = format(int(hexstr, 16), '08b')
#         binary.append(binary_str)
    
#     for i in range(binary):
#         b+= str(binary(i))

#     return b


# input_hex = ['1F', 'A0', '0B', 'FF']
# output_binary = tobinary(reversed(input_hex))
# print((output_binary))  # ['00011111', '10100000', '00001011', '11111111']
# print(hex(0xffffffffffffffff + 0x90abcdef90abcdef))


# a = ['3e', '84', 'be', 'dc', 'ac', '0d', '59', '80', 'd3', '0f', '8b', 'e4', '54', 'a9', '3d', 'cc', 'c5', '72', '9b', 'ec', 'cd', '5f', '5b', 'e0', 'b8', '49', '79', '00', 'f9', 'e3', '1c', 'e5', '3e', '4f', '96', 'f8', 'fc', 'bf', 'ad', 'd3', 'd0', '72', '8b', 'dd', '03', '72', '20', '37', '4a', '1c', '3a', '7f', '52', 'da', 'ef', 'cb', '4f', '49', '78', '8c', '37', '7e', '0b', '41', '9c', '68', '3d', '30', '89', '97', 'b7', '57', '3c', '5f', 'a5', '83', '37', 'c9', '0e', 'd6', '3c', 'df', '02', '4d', 'b0', '61', '33', 'ac', 'c3', '20', 'c0', '89', 'b2', '0c', 'ef', '0c']
# b= ['3e', '84', 'be', 'dc', 'ac', '0d', '59', '80', 'd3', '0f', '8b', 'e4', '54', 'a9', '3d', 'cc', 'c6', '72', '9b', 'ec', 'cd', '5f', '5b', 'e0', 'b8', '49', '79', '00', 'f9', 'e3', '1c', 'e5', '3c', '4f', '96', 'f8', 'fc', 'bf', 'ad', 'd3', 'd2', '72', '8b', 'dd', '03', '72', '20', '37', '49', '1c', '3a', '7f', '52', 'da', 'ef', 'cb', '4d', '49', '78', '8c', '37', '7e', '0b', '41', '9e', '68', '3d', '30', '89', '97', 'b7', '57', '3a', '5f', 'a5', '83', '37', 'c9', '0e', 'd6', '39', 'df', '02', '4d', 'b0', '61', '33', 'ac', 'c3', '20', 'c0', '89', 'b2', '0c', 'ef', '0c']
# list =[]
# for i in range(len(a)):
#     if a[i] != b[i]:
#         list.append(i)
# print(list)

print(hex(0x1c0c1d729 * 0xda9fa5a3))
