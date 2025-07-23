You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            return self.remove(s, 'b', 'a', y, x)  
        else:
            return self.remove(s, 'a', 'b', x, y)  

    def remove(self, s: str, first: str, second: str, first_points: int, second_points: int) -> int:
        score = 0
        stack = []

        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                score += first_points
            else:
                stack.append(ch)
        final_stack = []
        for ch in stack:
            if final_stack and final_stack[-1] == second and ch == first:
                final_stack.pop()
                score += second_points
            else:
                final_stack.append(ch)

        return score  


optimez code 
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Always remove the higher value pair first
        if x < y:
            s, score = self.remove_pairs(s, 'b', 'a', y)
            _, second_score = self.remove_pairs(s, 'a', 'b', x)
        else:
            s, score = self.remove_pairs(s, 'a', 'b', x)
            _, second_score = self.remove_pairs(s, 'b', 'a', y)
        return score + second_score

    def remove_pairs(self, s: str, first: str, second: str, points: int) -> (str, int):
        stack = []
        score = 0
        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                score += points
            else:
                stack.append(ch)
        return ''.join(stack), score
