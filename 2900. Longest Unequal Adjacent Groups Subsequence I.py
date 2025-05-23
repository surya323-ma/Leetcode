You are given a string array words and a binary array groups both of length n.
A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements at the same indices in groups are different (that is, there cannot be consecutive 0 or 1).
Your task is to select the longest alternating subsequence from words.
Return the selected subsequence. If there are multiple answers, return any of them.
Note: The elements in words are distinct.
#codehere
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        if n == 1:
            return words  # If there's only one word, return it as the sequence.
        
        # Initialize the longest subsequence with the first word
        subseq = [words[0]]
        last_group = groups[0]

        for i in range(1, n):
            if groups[i] != last_group:
                subseq.append(words[i])
                last_group = groups[i]
        
        return subseq
