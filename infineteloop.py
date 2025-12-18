import numpy as np

arr=np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
             [['j','k','l'],['m',',n','o'],['p','q','r']],
             [['s','t','u'],['v','w','x'],['y','z',' ']]])

word = arr[0,0,0]+arr[1,2,0]+arr[1,2,0]+arr[1,0,2]+arr[0,1,1]

print(word)