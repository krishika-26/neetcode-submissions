class Solution:
    def minEatingSpeed(self, p, h):
        l, r = 1, max(p)
        while l < r:
            m = (l + r) // 2
            if sum((x + m - 1) // m for x in p) <= h: r = m
            else: l = m + 1
        return l