
def from8(list): 
    reversedlist = reversed(list)
    hexstring = ''.join(reversedlist)
    if hexstring.startswith('0') and len(hexstring) % 2 != 0:
        hexstring = hexstring[1:]
    
    return (int(hexstring,16))

a= ['da','01']
print(hex(from8(a)))