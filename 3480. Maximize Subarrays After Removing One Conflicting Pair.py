You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs, where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

Remove exactly one element from conflictingPairs. Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any remaining conflicting pair [a, b].

Return the maximum number of subarrays possible after removing exactly one conflicting pair.

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        conflicts = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            conflicts[max(a, b)].append(min(a, b))
        max_left = second_max_left = valid_subarrays = 0
        gains = [0] * (n + 1)
        for right in range(1, n + 1):
            for left in conflicts[right]:
                if left > max_left:
                    second_max_left = max_left
                    max_left = left
                elif left > second_max_left:
                    second_max_left = left

            valid_subarrays += right - max_left
            gains[max_left] += max_left - second_max_left

        return valid_subarrays + max(gains)
