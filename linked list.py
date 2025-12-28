class Numbers(object):
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2


# create object
obj = Numbers()

# input
b = int(input("Enter first number: "))
c = int(input("Enter second number: "))

# method calls
print("Addition:", obj.add(b, c))
print("Subtraction:", obj.sub(b, c))
