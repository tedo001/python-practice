 def sort(num):
     pivot=num[0]
     left=[]
     right=[]
     for i in range(len(num)-1):
         if num[i+1]<pivot:
             left.append(num[i])
             right.append(num[i+1])
     return left+right

