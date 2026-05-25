class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp not in seen:
                seen[n] = i
            else :
                return [seen[comp], i]