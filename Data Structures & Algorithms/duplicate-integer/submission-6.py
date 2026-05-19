class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## using set
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False