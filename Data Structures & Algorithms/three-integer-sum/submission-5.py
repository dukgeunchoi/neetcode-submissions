class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: continue

            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if ([nums[i], nums[l], nums[r]]) not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        
        return res
        