A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(num):
            digits = []
            while num:
                digits.append(str(num % k))
                num //= k
            return ''.join(reversed(digits))

        def generate_palindromes(length, odd=True):
            # Half-length generation to create full palindromes
            start = 10 ** ((length - 1) // 2)
            end = 10 ** ((length + 1) // 2)
            for half in range(start, end):
                half_str = str(half)
                if odd:
                    yield int(half_str + half_str[-2::-1])
                else:
                    yield int(half_str + half_str[::-1])

        count = 0
        total = 0
        length = 1

        while count < n:
            for num in generate_palindromes(length, odd=(length % 2 == 1)):
                if is_palindrome(to_base_k(num)):
                    total += num
                    count += 1
                    if count == n:
                        return total
            length += 1
