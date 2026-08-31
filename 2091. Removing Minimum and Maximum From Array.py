You are given a 0-indexed array of distinct integers nums.
There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.
A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.
Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.
class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        front = max(min_idx, max_idx) + 1
        back = n - min(min_idx, max_idx)
        both = min(min_idx + 1 + n - max_idx, max_idx + 1 + n - min_idx)        
        return min(front, back, both)
