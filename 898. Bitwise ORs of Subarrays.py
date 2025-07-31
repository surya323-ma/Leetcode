Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.

The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.

A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def subarrayBitwiseORs(self, arr):
        s = []  
        l=0
        for a in arr:  
            r = len(s)  
            s.append(a) 
            for i in range(l, r):
                v = s[i] | a
                if v != s[-1]:  
                    s.append(v)
            l = r
        return len(set(s)) 
   
