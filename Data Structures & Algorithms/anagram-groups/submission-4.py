class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i, s in enumerate(strs):
            sorted_s = "".join(sorted(s))
            hashmap[sorted_s].append(s)
        
        res = []
        for h in hashmap.values():
            res.append(h)
        return res