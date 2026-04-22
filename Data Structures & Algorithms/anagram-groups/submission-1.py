class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: return [strs]

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 ## rather than sorting every string, we can count array
            for char in s:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())
        
        
        # if len(strs) <= 1: return [strs]

        # anagrams = defaultdict(list)

        # for string in strs:
        #     sorted_str = ''.join(sorted(string))
        #     anagrams[sorted_str].append(string)
        
        # return list(anagrams.values())