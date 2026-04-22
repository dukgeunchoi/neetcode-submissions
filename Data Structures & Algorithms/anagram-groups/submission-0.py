class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: return [strs]

        anagrams = {}

        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(string)
        
        res = []
        for array in anagrams.values():
            res.append(array)
        return res