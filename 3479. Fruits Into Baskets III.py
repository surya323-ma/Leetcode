You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1
        tree = [0] * (2 * size)

        # load leaves
        for i, cap in enumerate(baskets):
            tree[size + i] = cap
        # build internals
        for k in range(size - 1, 0, -1):
            tree[k] = max(tree[2*k], tree[2*k+1])

        def query(x: int) -> int:
            if tree[1] < x:
                return -1
            k = 1
            while k < size:
                if tree[2*k] >= x:
                    k = 2*k
                else:
                    k = 2*k + 1
            return k - size

        def update(pos: int) -> None:
            k = pos + size
            tree[k] = 0
            k //= 2
            while k:
                tree[k] = max(tree[2*k], tree[2*k+1])
                k //= 2

        unplaced = 0
        for qty in fruits:
            idx = query(qty)
            if idx < 0:
                unplaced += 1
            else:
                update(idx)
        return unplaced
