You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []
        for spell in spells:
            min_potion = math.ceil(success / spell)
        # Find the first index where potion >= min_potion
            index = bisect.bisect_left(potions, min_potion)
        # Count of successful pairs
            result.append(m - index)
        return result
