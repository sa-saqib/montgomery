#missing element only with bit operator 
a=[8,6,4,7,3]
m=0
s=0
for i in range (0, len(a)):
    m^=a[i]
for i in range (3,9):
    s^= i
print(m^s)

