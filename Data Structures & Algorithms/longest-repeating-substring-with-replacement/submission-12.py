class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0
        res = 0
        for r in range(len(s)):
            curr_window_size = r + 1 - l
            seen[s[r]] = 1 + seen.get(s[r], 0)
            
            maxCount = 0
            for n in seen.values():
                maxCount = max(maxCount, n)
            
            if curr_window_size - maxCount > k:
                seen[s[l]] -= 1
                l += 1
                continue
            
            res = max(res, curr_window_size)
        
        return res