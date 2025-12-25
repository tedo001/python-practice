string=input("enter a string:")
rev=""
for i in string:
    rev=i+rev

if string==rev:
    print("string is a palindrome:",string)
else:
    print("string is not a palindrome")

    #s = input("Enter a string: ")
    #rev = ""

    #for ch in s:
     #   rev = ch + rev

    #if s == rev:
     #   print("Palindrome")
    #e#lse:
     #   print("Not Palindrome")
