class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        res = 0
        curr = 0

        while r < len(s):
            if s[r] not in seen:
                curr = r - l + 1
                seen.add(s[r])
                res = max(res, curr)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            r += 1
        return res

                