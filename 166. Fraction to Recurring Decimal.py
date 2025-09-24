Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        result.append(".")
        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break
            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result) 
