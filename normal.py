import numpy as np
x=np.array([[1,2,3],[2,3,4]])
y=np.array([[2,3,4],[2,3,4]])
bais=0.2
epoch=20
for i in range(epoch):
    mm=x*y+bais
    loss=mm-bais
    print(f"{"epoch",i+1,mm}{"loss function :",loss}")
