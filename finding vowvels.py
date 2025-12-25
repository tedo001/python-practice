string=input("enter a string")
count=0
for i in string:
    if i in "aeiouAEIOU":
        count+=1
print(count)