def into8(hex_string):
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string  
    byte_array = bytes.fromhex(hex_string)
    # print(byte_array)
    result = [f"{byte:02x}" for byte in reversed(byte_array)]
    return result

# input = "19a2cc4d84296d0b6fe94b3827dcf967baa95fbe812538a9f45bb542d2d0601588e9828144bab9f5865db57a9ff55ee3"
# output = into8(input)
# print(output)
# print(len(output))