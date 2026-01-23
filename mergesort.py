class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            cut1 = (left + right) // 2

            cut2 = (m + n + 1) // 2 - cut1

            leftA = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            rightA = float('inf') if cut1 == m else nums1[cut1]

            leftB = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            rightB = float('inf') if cut2 == n else nums2[cut2]

            if leftA <= rightB and leftB <= rightA:

                if (m + n) % 2 == 0:
                    left_max = max(leftA, leftB)
                    right_min = min(rightA, rightB)
                    return (left_max + right_min) / 2.0

                else:
                    return max(leftA, leftB)

            elif leftA > rightB:
                right = cut1 - 1

            else:
                left = cut1 + 1
