class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in numset: continue
            length = 1
            val = num
            while val + 1 in numset:
                length += 1
                val += 1
            longest = max(longest, length)
        
        return longest

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        numset = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in numset:
                continue
            length = 1
            while num + length in numset:
                length += 1
            longest = max(longest, length)
        
        return longest
