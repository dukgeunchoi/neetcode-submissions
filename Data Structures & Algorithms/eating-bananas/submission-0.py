class Solution:
    def calcEatingTime(self, piles: List[int], m: int) -> int:
        res = 0
        for p in piles:
            res += p // m
            s = p % m
            if s != 0: res += 1
        
        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l+r)//2

            if self.calcEatingTime(piles, m) <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

