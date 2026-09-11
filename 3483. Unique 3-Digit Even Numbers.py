You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.
from typing import List
from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = set()
        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:   # no leading zero, last digit even
                result.add(a*100 + b*10 + c)
        return len(result)

