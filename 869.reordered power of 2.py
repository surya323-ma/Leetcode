You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter
        def digit_count(x):
            return Counter(str(x))

        n_count = digit_count(n)

        for i in range(31):
            power_of_two = 1 << i
            if digit_count(power_of_two) == n_count:
                return True

        return False
