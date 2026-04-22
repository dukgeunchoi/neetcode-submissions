class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, count in count.items():
            freq[count].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            if freq[i] == 0: continue
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result

        
        # count = {}

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # res = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        # return list(res.keys())[:k]