class Solution(object):
    def removeDuplicates(self, nums):
        temp = nums[0]
        num2 = nums

        j = 1
        for i in range(len(num2)):
            temp = i
            for n in nums[i+1:]:
                if temp == n:
                    nums.remove(i)
        expectedNum = str(nums[1:] + nums[-1])
        return list(map(int(expectedNum)))
s=Solution()
inp=list(map(int,input()))
print(s.removeDuplicates([inp]))
