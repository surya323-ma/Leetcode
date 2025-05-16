You are given a string array words, and an array groups, both arrays having length n.

The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.

You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:

For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.
Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.

Note: strings in words may be unequal in length.

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        connections = {}
        maxs = {}
        result = []

        def HammingDistance(base, word):
            differences = 0
            
            if len(base) != len(word):
                return -1
            else:
                for i in range(len(word)):
                    if base[i] != word[i]: differences += 1
                    if differences > 2: return -1
            return differences

        for i in range(n):
            connections[i] = []
            for k in range(i, n):
                if groups[i] != groups[k] and HammingDistance(words[i], words[k]) == 1:
                    connections[i].append(k)
        
        for i in range(n - 1, -1, -1):
            maxs[i] = []

            for connection in connections[i]:
                if len(maxs[connection]) > len(maxs[i]):
                    maxs[i] = maxs[connection]
            
            maxs[i] = [words[i]] + maxs[i]
            if len(maxs[i]) > len(result):
                result = maxs[i]

        return result
                    

