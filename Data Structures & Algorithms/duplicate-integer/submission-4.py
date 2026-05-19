class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## using hashmap
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
            if hashmap[i] > 1: return True
        return False