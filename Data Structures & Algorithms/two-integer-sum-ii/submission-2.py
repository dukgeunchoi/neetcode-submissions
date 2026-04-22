class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i, n in enumerate(numbers):
            comp = target - n
            # if comp == n: continue

            if comp not in seen:
                seen[n] = i + 1
                continue
            
            return [seen[comp], i + 1]
            
