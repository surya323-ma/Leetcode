There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
nums[u] = nums[u] XOR k
nums[v] = nums[v] XOR k
Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.
#code here
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total_sum = sum(nums)
        deltas = [(num ^ k) - num for num in nums]
        deltas.sort(reverse=True)
        
        max_sum = total_sum
        for i in range(0, len(deltas) - 1, 2):
            delta_pair = deltas[i] + deltas[i + 1]
            if delta_pair > 0:
                max_sum += delta_pair
            else:
                break
        return max_sum
