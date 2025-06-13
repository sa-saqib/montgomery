def split(array):
    mid= len(array) //2
    return (array[:mid] , array[mid:]) if len(array)%2 ==0 else (array[:mid+1] , array[mid+1:]+['00']) 

# x = [32, 42,52,62, 72,82,92,12]

'''print(split(x)[0])
print(split(x)[1])'''