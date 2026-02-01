def sort(nums1,nums2):
    num3 = nums1+nums2
    num3.sort()
    count = 0
    try:

        for i in num3:
            count = count + i

    return count / len(num3)
num1 =list(input())
num2 =list(input())

sort(num1,num2)