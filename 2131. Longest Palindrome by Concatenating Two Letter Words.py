You are given an array of strings words. Each element of words consists of two lowercase English letters.
Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
A palindrome is a string that reads the same forward and backward.

 class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = {}
        max_len = 0
        middle = True
        for word in words:
            freq[word] = freq.get(word,0) + 1
        print(freq)
        for k in list(freq.keys()):
            if k[0] != k[1]:
                max_len += 4 * min(freq.get(k[1]+k[0], 0), freq[k])
            elif (freq[k]>1):
                if (freq[k] % 2==0):
                    max_len += 2 * freq[k]
                elif middle:
                    max_len += 2 * freq[k]
                    middle = False
                else:
                    max_len += 4 * (freq[k]//2)
            elif middle:
                max_len += 2
                middle = False
            del freq[k]
        return max_len
        
