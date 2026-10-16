You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD, n = 10**9 + 7, len(nums)
        t, s, lazy = [0]*(4*n), [0]*(4*n), [0]*(4*n)
        last, ans = {}, 0

        def upd(v, l, r, a, b):
            if a <= l and r <= b:
                s[v] += 2*t[v] + r-l+1
                t[v] += r-l+1
                lazy[v] += 1
                return
            m = (l+r)//2
            if lazy[v]:
                for c, x, y in ((2*v,l,m),(2*v+1,m+1,r)):
                    d = lazy[v] * (y-x+1)
                    s[c] += 2*lazy[v]*t[c] + lazy[v]**2*(y-x+1)
                    t[c] += d
                    lazy[c] += lazy[v]
                lazy[v] = 0
            if a <= m: upd(2*v,l,m,a,b)
            if b > m: upd(2*v+1,m+1,r,a,b)
            t[v] = t[2*v] + t[2*v+1]
            s[v] = s[2*v] + s[2*v+1]

        for i, x in enumerate(nums):
            upd(1,0,n-1,last.get(x,-1)+1,i)
            last[x] = i
            ans = (ans+s[1]) % MOD
        return ans
