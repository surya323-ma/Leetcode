You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
#code here
  class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        for digit in num_str:
            if digit != '9':
                max_num = int(num_str.replace(digit, '9'))
                break
        else:
            max_num = num
        for digit in num_str:
            if digit != '0':
                min_num = int(num_str.replace(digit, '0'))
            break
        else:
            min_num = num
    
        return max_num - min_num
