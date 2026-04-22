class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        max_h = 0
        for i, h in enumerate(height):
            maxLeft[i] = max_h
            max_h = max(max_h, height[i])
        
        max_h = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = max_h
            max_h = max(max_h, height[i])

        max_trapped = 0
        for i in range(len(height)):
            # if maxLeft[i] == 0 or maxRight[i] == 0 or maxLeft[i] < height[i] or maxRight[i] < height[i]: continue
            curr_max = min(maxLeft[i], maxRight[i]) - height[i]
            if curr_max < 0: curr_max = 0
            max_trapped += curr_max
        return max_trapped