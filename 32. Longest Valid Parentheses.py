Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring
#code here
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        ans=0
        stack.append(-1)
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)!=0:
                    ans=max(ans,i-stack[-1])
                else:
                    stack.append(i)
        return ans 
