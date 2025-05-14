You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

#code here
from collections import defaultdict
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        m=10**9+7
        def mat_mult(a,b):
            res=[[0]*26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        res[i][j]=(res[i][j]+a[i][k]*b[k][j])%m
            return res
        def mat_pow(mat,p):
            res=[[int(i==j) for j in range(26)] for i in range(26)]
            while p:
                if p&1:
                    res=mat_mult(res,mat)
                mat=mat_mult(mat,mat)
                p>>=1
            return res
        T=[[0]*26 for _ in range(26)]
        for i in range(26):
            for j in range(nums[i]):
                T[i][(i+j+1)%26]+=1
        T=mat_pow(T,t)
        r=0
        for ch in s:
            idx=ord(ch)-ord('a')
            r=(r+sum(T[idx]))%m
        return r     
