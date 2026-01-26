

sttr="hello world"
num=0
for i in range(len(sttr)):
    if sttr[i] in "aeiou":
       num=num+1
       continue

print(num)