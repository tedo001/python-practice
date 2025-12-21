name = "Tedo"
city = 'Coimbatore'
s1 = "hello"
s2 = 'python'
s3 = """this is
multi line
string"""
# accessing char(indexing)
word = "python"

print(word[0])   # p
print(word[3])   # h
print(word[-1])  # n (last character)

#string lenth
print(len(word))   # 6

#string slicing
word = "python"

print(word[0:3])   # pyt
print(word[2:])    # thon
print(word[:4])    # pyth
print(word[::-1])  # nohtyp (reverse)

#string are imuttable
# wrong word[0] = 'P'
word = 'P' + word[1:]

#string concatenation
a = "Hello"
b = "World"

print(a + " " + b)

# repeating string
print("ha" * 3)

#lower and upper case char
text = "Python"
print(text.lower())  # python
print(text.upper())  # PYTHON

#remove space strip()
msg = "  hello  "
print(msg.strip())

#replace
print("hello world".replace("world", "python"))

#string split
data = "apple,banana,orange"
print(data.split(","))

#find()
print("python".find("t"))  # 2

#count()
print("banana".count("a"))  # 3

#check string type by boolean
print("abc".isalpha())   # True
print("123".isdigit())   # True
print("abc123".isalnum()) # True

#string formatting
#f-string
name = "Tedo"
age = 20

print(f"My name is {name} and age is {age}")

#looping through string

for ch in "python":
    print(ch)

#real example with using a input and string
email = input("Enter email: ")

if "@gmail.com" in email:
    print("Valid email")
else:
    print("Invalid email")
