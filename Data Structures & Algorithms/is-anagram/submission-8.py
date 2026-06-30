class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sMap = {}
        tMap = {}

        for i in s:
            sMap[i] = 1 + sMap.get(i, 0)
        for j in t:
            tMap[j] = 1 + tMap.get(j, 0)
        return sMap == tMap

