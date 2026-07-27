class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for n in nums:
            curr_res = 1
            curr = n + 1
            while curr in numset:
                curr_res += 1
                curr += 1
            res = max(res, curr_res)
        
        return res

        