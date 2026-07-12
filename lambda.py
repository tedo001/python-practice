from numpy import random
weight= random.rand(4,3)
input_=[23,4,5]
bais=0.2
y=input_ * weight + bais
 #relu=max(0,y)
print(y)
