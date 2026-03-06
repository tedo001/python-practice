class fruits:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name,self.price)
n="apple"
b=1234
f=fruits()
f.display(n,b)