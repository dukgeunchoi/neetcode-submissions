class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr = min(heights[l], heights[r]) * (r-l)
            area = max(area, curr)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                # if heights[l+1] < heights[r-1]:
                #     r -= 1
                # else:
                #     l += 1
        
        return area
            