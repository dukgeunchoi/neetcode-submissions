class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        nonZeroProduct = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                nonZeroProduct *= num
            totalProduct *= num
        res = []
        for num in nums:
            if num == 0:
                if zeroCount > 1: 
                    res.append(0)
                else:
                    res.append(nonZeroProduct)
                continue
            n = totalProduct / num
            res.append(int(n))
        return res