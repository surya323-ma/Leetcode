You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)

        low, high = 0, nums[-1] - nums[0]

        # Step 3: Binary search
        while low < high:
            mid = (low + high) // 2

            # Step 4: Try to form pairs
            count = 0
            i = 1
            while i < n and count < p:
                if nums[i] - nums[i - 1] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1

            # Binary search update
            if count >= p:
                high = mid
            else:
                low = mid + 1

        # Step 5: Return result
        return low
