class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Set = {}
        for s in s1:
            s1Set[s] = s1Set.get(s, 0) + 1

        l = 0
        seen = {}
        for r, s in enumerate(s2):
            if s not in s1Set:
                if seen:
                    seen.clear()
                l = r + 1
            if s in s1Set:
                seen[s] = seen.get(s, 0) + 1
                while seen.get(s) > s1Set.get(s):
                    seen[s2[l]] -= 1
                    l += 1
                print(seen)
                if seen == s1Set: return True
                
        return False