You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.
class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0

        # Shift img1 by (dr, dc)
        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                overlap = 0

                for r in range(n):
                    for c in range(n):
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < n and 0 <= nc < n:
                            if img1[r][c] == 1 and img2[nr][nc] == 1:
                                overlap += 1

                ans = max(ans, overlap)

        return ans
