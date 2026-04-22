import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            bites = 0
            for p in piles:
                bites += math.ceil(p / m)
            
            if bites <= h:
                res = min(res, m)
                r = m - 1
            elif bites > h:
                l = m + 1
            
        return res