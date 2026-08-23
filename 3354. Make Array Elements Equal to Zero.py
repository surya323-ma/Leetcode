You are given an integer array nums.

Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.

After that, you repeat the following process:

If curr is out of the range [0, n - 1], this process ends.
If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
Else if nums[curr] > 0:
Decrement nums[curr] by 1.
Reverse your movement direction (left becomes right and vice versa).
Take a step in your new direction.
A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.

Return the number of possible valid selections.

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(start, direction):
            n = len(nums)
            curr = start
            dir = direction  # 1 for right, -1 for left
            nums_copy = nums[:]
            while 0 <= curr < n:
                if nums_copy[curr] == 0:
                    curr += dir
                else:
                    nums_copy[curr] -= 1
                    dir *= -1
                    curr += dir

            return all(x == 0 for x in nums_copy)

        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if simulate(i, 1):  # right
                    count += 1
                if simulate(i, -1):  # left
                    count += 1

        return count
