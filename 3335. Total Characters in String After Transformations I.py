You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7
#code here
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        q = deque(itemgetter(*ascii_lowercase)(Counter(s))) 
        for _ in range(t):
            q.appendleft(q.pop()) 
            q[1] += q[0] 
        
        return sum(q)%(10**9 + 7)
