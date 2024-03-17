# maximum path from 00 to lenlen

input =[
    [3, 7, 9, 2, 7],
    [9, 8, 3, 5, 5],
    [1, 7, 9, 8, 5],
    [3, 8, 6, 4, 10],
    [6, 3, 9, 7, 8]
]

m = {}
m[(0,0)] = input[0][0]
from sys import maxsize

def f(i,j):
    if i<0 or j<0:
        # return maxsize
        return 0
    try :
        return m[(i,j)]
    except:
        m [(i,j)] = max([input[i][j]+f(i-1,j),input[i][j]+f(i,j-1)])
        return m[(i,j)]
    
print (f(len(input)-1,len(input[0])-1))
