You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Choose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i], basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = Counter(basket1 + basket2)
        for val in total:
            if total[val] % 2 != 0:
                return -1

    # Find excess fruits
        excess = []
        for val in total:
            diff = count1[val] - count2[val]
            if diff > 0:
                excess.extend([val] * (diff // 2))
            elif diff < 0:
                excess.extend([val] * (-diff // 2))

        excess.sort()
        min_cost = min(total.keys())
        cost = 0
        for i in range(len(excess) // 2):
            cost += min(excess[i], 2 * min_cost)
        return cost
