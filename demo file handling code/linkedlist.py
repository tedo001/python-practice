from numbers import Numbers

class LinkedList:
    def __init__(self):
        self.calc = Numbers()

    def calculate(self, x, y):
        print("Add:", self.calc.add(x, y))
        print("Sub:", self.calc.sub(x, y))
        print("Mul:", self.calc.multiply(x, y))
        print("Div:", self.calc.divide(x, y))


ll = LinkedList()

b = int(input("Enter first number: "))
c = int(input("Enter second number: "))

ll.calculate(b, c)
