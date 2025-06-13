def into8(hex_string):
       
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string    
    byte_array = bytes.fromhex(hex_string) 
    print(byte_array)   
    result = [f"{byte:02x}" for byte in reversed(byte_array)] 
    return result

 
# input = "44efb931608c078de7e94c4acd313c4ecc3da954e48b0fd380590dacdcbe843e"
# output = into8(input)
# print(output)
# print(len(output))  

 