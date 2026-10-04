Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


 class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                if low > 0:
                    low -= 1
                high -= 1
                if high < 0:
                    return False
            else:  # '*'
                if low > 0:
                    low -= 1
                high += 1

        return low == 0
