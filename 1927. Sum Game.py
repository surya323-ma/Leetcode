Alice and Bob take turns playing a game, with Alice starting first.

You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:

Choose an index i where num[i] == '?'.
Replace num[i] with any digit between '0' and '9'.
The game ends when there are no more '?' characters in num.

For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        diff = 0
        q1 = q2 = 0
        
        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                diff += int(num[i])
        
        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                diff -= int(num[i])
        
        # If odd number of '?', Alice wins
        if (q1 + q2) % 2 == 1:
            return True
        
        # Bob wins only if balance is achievable
        return diff != 9 * (q2 - q1) // 2
