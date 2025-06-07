You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

import heapq
from collections import defaultdict

class Solution:
    def clearStars(self, s):
        pq = []  # Min-heap for characters
        index_map = defaultdict(list)  # Map character -> list of indices
        keep = [True] * len(s)  # Marks whether to keep characters

        # Traverse the string
        for i, char in enumerate(s):
            if char == '*':
                if pq:
                    smallest = heapq.heappop(pq)  # Get smallest character
                    idx = index_map[smallest].pop()  # Remove last occurrence index
                    keep[i] = keep[idx] = False  # Mark for removal
            else:
                heapq.heappush(pq, char)
                index_map[char].append(i)

        # Build and return the result
        return "".join(s[i] for i in range(len(s)) if keep[i])
