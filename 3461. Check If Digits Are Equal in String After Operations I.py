You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:
For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
Return true if the final two digits in s are the same; otherwise, return false.

 class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s) != 2):
            temp = ""
            i = 0
            while(i < len(s) - 1):
                temp += str((int(s[i]) + int(s[i + 1])) % 10)
                i += 1
            s = temp
        if(s[0] == s[1]):
            return True
        else:
            return False
