You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.
from typing import List

class Solution:
    def minTime(self, skills: List[int], energy: List[int]) -> int:
        n, m = len(skills), len(energy)
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + skills[i]

        total = skills[0] * energy[0]
        for j in range(1, m):
            max_time = skills[0] * energy[j]
            for i in range(1, n):
                max_time = max(max_time, prefix[i] * energy[j - 1] - prefix[i - 1] * energy[j])
            total += max_time

        return total + prefix[-1] * energy[-1]
