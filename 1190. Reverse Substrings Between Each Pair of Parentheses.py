You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

  class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            elif c == ')':
                j = st.pop()
                s = s[:j] + s[j+1:i][::-1] + s[i+1:]
                return self.reverseParentheses(s)
        return s
