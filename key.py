import numpy as np 
x=np.array([[2,3,4],[4,5,6]])
w=np.array([[2,4,5],[5,6,7]])
b=0.1
nn=(x*w)+b
print(nn)
act=max(0,nn)
print("model nn is:",act)
