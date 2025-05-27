You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
#code here
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = [num for num in range(1, n + 1) if num % m]
        num2 = [num for num in range(1, n + 1) if not num % m]

        return sum(num1) - sum(num2)
