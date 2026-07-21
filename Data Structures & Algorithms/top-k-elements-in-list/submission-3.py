class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in  range(len(nums) + 1)]

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        for num, count in hashmap.items():
            if freq[count]:
                freq[count].append(num)
            else:
                freq[count] = [num]
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            if freq[i] == []: continue
            for j in freq[i]:
                res.append(j)
                if len(res) == k: return res
        