class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        for c in s1:
            s1Map[c] = 1 + s1Map.get(c, 0)
        
        seen = {}
        l = 0
        
        for r in range(len(s2)):
            if s2[r] in s1Map:
                if s1Map[s2[r]] == seen.get(s2[r], 0):
                    while s1Map[s2[r]] == seen[s2[r]]:
                        seen[s2[l]] -= 1
                        l += 1
            
                seen[s2[r]] = 1 + seen.get(s2[r], 0)

                print(l,r)
                if r - l + 1 == len(s1): return True
            else:
                l = r + 1
                seen.clear()
        
        return False
            
        