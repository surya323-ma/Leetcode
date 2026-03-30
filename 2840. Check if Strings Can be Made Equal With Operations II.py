You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

from collections import Counter

class Solution(object):
    def checkStrings(self, s1, s2):
        return (Counter(s1[::2]) == Counter(s2[::2]) and 
                Counter(s1[1::2]) == Counter(s2[1::2]))
        
