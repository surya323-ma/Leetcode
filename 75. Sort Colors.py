Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
code here
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        while(l<len(nums)):
            while(l<r):
                if nums[l]<nums[r]:
                    r-=1
                elif nums[l]>nums[r]:
                    nums[l],nums[r]=nums[r],nums[l]
                    r-=1
                else:
                    r-=1
            l+=1
            r=len(nums)-1
        return nums        
