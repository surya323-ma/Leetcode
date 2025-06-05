You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
#code here
from collections import defaultdict

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        adj = defaultdict(list)

        # Step 1: Build the graph
        for a, b in zip(s1, s2):
            adj[a].append(b)
            adj[b].append(a)

        def dfs(ch, visited):
            visited.add(ch)
            min_ch = ch
            for nei in adj[ch]:
                if nei not in visited:
                    candidate = dfs(nei, visited)
                    min_ch = min(min_ch, candidate)
            return min_ch

        result = []
        for ch in baseStr:
            visited = set()
            result.append(dfs(ch, visited))
        
        return ''.join(result)
