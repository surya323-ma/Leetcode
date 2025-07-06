You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
Implement the FindSumPairs class:

FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.dic=defaultdict(int)
        for i in nums1:
            self.dic[i]+=1
        self.arr=[k for k in nums2]
        self.dic2=defaultdict(int)
        for i in nums2:
            self.dic2[i]+=1

    def add(self, index: int, val: int) -> None:
        old=self.arr[index]
        self.arr[index]+=val
        self.dic2[old]-=1
        self.dic2[old+val]+=1

    def count(self, tot: int) -> int:
        ans=0
        for i in self.dic:
            ans+=self.dic2[tot-i]*(self.dic[i])
        return ans
