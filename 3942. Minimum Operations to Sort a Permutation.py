You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.

You may perform only the following operations:

Reverse the entire array.
Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

  class Solution:
    def minOperations(self, nums):
        n = len(nums)

        # Rotation form
        k = nums[0]
        if all(nums[i] == (k + i) % n for i in range(n)):
            if k == 0:
                return 0
            return min(n - k, k + 2)

        # Reversed-rotation form
        if all(nums[i] == (nums[0] - i) % n for i in range(n)):
            k = (nums[0] + 1) % n
            return min(k + 1, n - k + 1)

        return -1
