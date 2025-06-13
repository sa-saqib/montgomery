
from karatfor256 import karatfor256
from karatfor384 import karatfor384


def mulwinv(a,s):
    result=[]
    if s == 32:
        x = ['ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'fe', 'ff',
             'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'ff', 'fd', 'ff', 'ff', 'ff']
        result = karatfor256(a,s)
        
    elif s == 48: 
        x =  ['01', '00', '00', '00', '01', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', 'fe', 'ff', 'ff', 'ff', 'fb', 'ff', 
              'ff', 'ff', 'fa', 'ff', 'ff', 'ff', 'fc', 'ff', 'ff', 'ff', '02', '00', '00', '00', '0c', '00', '00', '00', '14', '00', '00', '00', '14']
        result = karatfor384(a,s)
    else:
        result = a

    return result    
