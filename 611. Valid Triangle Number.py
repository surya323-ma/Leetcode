Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for k in range(len(nums) - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count
