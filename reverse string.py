s=input("enter a string:")
reverse_s = s[::-1]
print(reverse_s)

s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev

print("Reversed string:", rev)

#using a reverse()
s = input("Enter a string: ")
rev = "".join(reversed(s))
print(rev)
