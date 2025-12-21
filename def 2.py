#################################
def add(x,y=50):
    print('x:',x)
    print('y:',y)
add(10)
print(add(12))
#################################
def todo(eating,studing):
    print(eating,studing)
todo(eating=10,studing=20)
todo(studing=20,eating=10)
###################################
def sums(add,sub):
    print(add,sub)
    print(add+sub)
print("case")
sums(add=10,sub=20)
print("\ncase2")
sums(add=21,sub=20)
####################################
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")
######################################