You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.
class Solution:
    def checkOverlap(self, r: int, x: int, y: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        dx = max(x1 - x, 0, x - x2)
        dy = max(y1 - y, 0, y - y2)
        return dx*dx + dy*dy <= r*r
