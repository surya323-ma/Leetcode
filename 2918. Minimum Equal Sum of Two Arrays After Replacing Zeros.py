You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.
#code here
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2, z1, z2 = 0, 0, 0, 0
        for x in nums1:
            if x == 0:
                z1 += 1
            else:
                s1 += x
        for x in nums2:
            if x == 0:
                z2 += 1
            else:
                s2 += x
        s1 += z1
        s2 += z2
        if s1 < s2 and z1 == 0 or s2 < s1 and z2 == 0:
            return -1
        return max(s1, s2)
