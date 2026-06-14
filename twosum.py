def  twosum(nums,target):
    for i, j in enumerate(nums):
        com = target - j
        if com in nums and com != nums[i]:
            ind = nums.index(com)
            return i, ind
        else:
            continue


nums=[3,3]
target=6

print(twosum(nums,target))