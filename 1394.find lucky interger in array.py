Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

 class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = [0] * 501
        for n in arr:
            freq[n] += 1
        for i in range(500, 0, -1):
            if freq[i] == i:
                return i  
        return -1
