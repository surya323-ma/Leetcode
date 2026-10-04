You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].
You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.
The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.
For each query in queries you need to determine the x-value of nums for xi after performing the following actions:
Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).
Return an array result of size queries.length where result[i] is the answer for the ith query.
A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.
A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.
Note that the prefix and suffix to be chosen for the operation can be empty.
Note that x-value has a different definition in this version.

 class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        s = 1 << (n - 1).bit_length()
        tree = [([0] * k, 1) for _ in range(2 * s)]

        def merge(a, b):
            c, p = a
            d, q = b
            cnt = c[:]
            for r in range(k):
                cnt[p * r % k] += d[r]
            return cnt, p * q % k

        for i, v in enumerate(nums):
            c = [0] * k
            c[v % k] = 1
            tree[s + i] = (c, v % k)

        for i in range(s - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(i, v):
            i += s
            c = [0] * k
            c[v % k] = 1
            tree[i] = (c, v % k)
            while i > 1:
                i //= 2
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def query(l, r):
            a, b = ([0] * k, 1), ([0] * k, 1)
            l += s
            r += s
            while l < r:
                if l & 1:
                    a = merge(a, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    b = merge(tree[r], b)
                l //= 2
                r //= 2
            return merge(a, b)[0]

        ans = []
        for i, v, l, x in queries:
            update(i, v)
            ans.append(query(l, n)[x])
        return ans
