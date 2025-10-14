You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

Count the number of pairs of points (A, B), where

A is on the upper left side of B, and
there are no other points in the rectangle (or line) they make (including the border), except for the points A and B.
class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        result = 0

        for i in range(n):
            top = points[i][1]
            bot = float("-inf")
            for j in range(i + 1, n):
                y = points[j][1]
                if bot < y <= top:
                    result += 1
                    bot = y
                    if bot == top:
                        break
        return result
