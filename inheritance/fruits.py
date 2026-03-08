class fruits:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name)
        print(self.price)
f=str(input("enter a fruit name:"))
p=int(input(f"enter a price of a {f} fruit:"))
f=fruits(f,p)
f.display()