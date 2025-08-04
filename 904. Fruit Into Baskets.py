You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        max_fruits = 0
        for right, fruit in enumerate(fruits):
            count[fruit] += 1

        # If more than two types, shrink from the left
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

        # Update the maximum window size
            current_window = right - left + 1
            max_fruits = max(max_fruits, current_window)
        return max_fruits
