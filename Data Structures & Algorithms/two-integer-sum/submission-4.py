class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            print(seen)
            comp = target - n
            print(comp)
            if comp not in seen:
                seen[n] = i
                continue
            return [seen[comp], i]
        
