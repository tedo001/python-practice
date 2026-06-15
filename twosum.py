def  twosum(nums,target):
    for i, j in enumerate(nums):
        com = target - j
        if com in nums and com is not  nums[i]:
            ind = nums.index(com)
            return i, ind
        elif com in nums[1:]:
            nums[:]= nums[1:]
            c=nums.index(com)
            return i,c

            continue


nums=[3,3]
target=6

print(twosum(nums,target))