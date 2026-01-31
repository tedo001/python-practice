def sort(num):
     pivot=num[0]
     left=[]
     right=[]
     for i in range(len(num[1:])):
         if num[i]>pivot:
             left.append(num[i])
         elif num[i]<pivot:
             right.append(num[i])
         else:
             return num
     return sort.left + sort.pivot + sort.right
num="876392"
sort(num)
