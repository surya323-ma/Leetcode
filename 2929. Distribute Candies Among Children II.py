You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies
#code here
  class Solution:
    def cal(self, x: int) -> int:
        if x < 0:
            return 0
        return x * (x - 1) // 2

    def distributeCandies(self, n: int, limit: int) -> int:
        return (self.cal(n + 2) - 3 * self.cal(n - limit + 1) +
                3 * self.cal(n - (limit + 1) * 2 + 2) - self.cal(n - 3 * (limit + 1) + 2))
