class Numbers(object):
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2


obj = Numbers()

b = int(input("Enter first number: "))
c = int(input("Enter second number: "))

print("Addition:", obj.add(b, c))
print("Subtraction:", obj.sub(b, c))
