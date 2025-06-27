You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.

For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.
#code here
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isSubSeq(s,t):
            i = j = 0
            m = len(s)
            n = len(t)

            while i < m and j < n:
                if s[i] == t[j]:
                    j += 1
                i += 1
            return j == n
        n = len(s)
        count = Counter(s)
        allowedCount = defaultdict(int)

        for c , cnt in count.items():
            if cnt >= k:
                allowedCount[c] = cnt//k
        sortedLetters = sorted(allowedCount.keys() , reverse=True)

        cand = []
        for c in sortedLetters:
            cnt = defaultdict(int)
            cnt[c] += 1
            cand.append((c,cnt))
        while True:
            newCand = []
            for cur , cnt in cand:
                for c in sortedLetters:
                    allowedCnt = allowedCount[c]
                    if cnt[c] < allowedCnt:
                        if isSubSeq(s, (cur+c)*k):
                            newCnt = cnt.copy()
                            newCnt[c] += 1
                            newCand.append((cur+c, newCnt))
            if not newCand:
                break
            cand = newCand
        return cand[0][0] if cand else ""
        
