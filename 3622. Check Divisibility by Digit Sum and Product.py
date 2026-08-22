You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

The digit sum of n (the sum of its digits).

The digit product of n (the product of its digits).

Return true if n is divisible by this sum; otherwise, return false.

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = list(map(int, str(n)))
        digit_sum = sum(digits)
        digit_product = 1
        for d in digits:
            digit_product *= d
    
        divisor = digit_sum + digit_product
        return n % divisor == 0
