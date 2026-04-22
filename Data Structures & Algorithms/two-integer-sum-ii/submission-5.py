class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # seen = defaultdict(int)

        # for i, n in enumerate(numbers):
        #     comp = target - n
        #     # if comp == n: continue

        #     if comp not in seen:
        #         seen[n] = i + 1
        #         continue
            
        #     return [seen[comp], i + 1]
            
