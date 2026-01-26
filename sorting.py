def sort(arr):
    if len(arr)<1:
        return arr
    pivot = arr[0]
    left=[]
    right=[]
    for num in arr:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return sort(left) + [pivot] + sort(right)
num = list(map(int, input("Enter a number: ")))
num.sort()
print("Sorted digits:", num)