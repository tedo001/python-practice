digits=[1,2,3]
f=[]
for i in digits:
    num=1+digits[-1]
    f.append(num)
    break
digits.pop(-1)
digits.append(f)
print(digits)

