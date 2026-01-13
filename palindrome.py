string=input("enter a String:")
rev=""
for i in string:
    rev=i+rev

if string==rev:
    print("string is a palindrome:",string)
else:
    print("string is not a palindrome")

