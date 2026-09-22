class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 1000
        while l <= r:
            m = (l+r) // 2
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                return res
            elif nums[m] < nums[l]:
                res = min(res,nums[m])
                r = m - 1
            elif nums[m] >= nums[l]:
                res = min(res,nums[m])
                l = m + 1

        return res