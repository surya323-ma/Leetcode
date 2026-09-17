You are given a string s and a positive integer k.
Select a set of non-overlapping substrings from the string s that satisfy the following conditions:
The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.
A substring is a contiguous sequence of characters within a string.

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n, res, last = len(s), 0, -1
        pals = []
        for i in range(n):
            for l, r in ((i,i),(i,i+1)):
                while l>=0 and r<n and s[l]==s[r]:
                    if r-l+1>=k: pals.append((l,r))
                    l-=1; r+=1
        for l,r in sorted(pals,key=lambda x:x[1]):
            if l>last: res+=1; last=r
        return res
