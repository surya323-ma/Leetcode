Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
#code here
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True 
        for j in range(2, len(p) + 1): 
            if p[j - 1] == '*': dp[0][j] = dp[0][j - 2] 
        for i in range(1, len(s) + 1): 
            for j in range(1, len(p) + 1): 
                if p[j - 1] == '*': 
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.') )            
                else: 
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '.') 
        return dp[len(s)][len(p)]
