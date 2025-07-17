You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)] 
        maxLength = 0
        for num in nums:
            current_rem = num % k
            for prev_rem in range(k):
                dp[prev_rem][current_rem] = dp[current_rem][prev_rem] + 1
                maxLength = max(maxLength, dp[prev_rem][current_rem])
        return maxLength
