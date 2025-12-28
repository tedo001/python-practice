class Numbers:
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2
    def mul(self, num1, num2):
        return num1 * num2
    def div(self, num1, num2):
        return num1 / num2
    def pow(self, num1, num2):
        return num1 ** num2


class LinkedList:
    def __init__(self):
        self.calc = Numbers()

    def calculate(self, x, y):
        print("Add:", self.calc.add(x, y))
        print("Sub:", self.calc.sub(x, y))


ll = LinkedList()

b = int(input("Enter first number: "))
c = int(input("Enter second number: "))

ll.calculate(b, c)
