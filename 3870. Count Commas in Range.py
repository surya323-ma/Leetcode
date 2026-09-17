You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.
  class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1000
        commas = 1

        while start <= n:
            end = min(n, start * 1000 - 1)

            count = end - start + 1
            ans += count * commas

            start *= 1000
            commas += 1

        return ans
