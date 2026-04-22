class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s)) ## O(nlogn)
            anagrams[sorted_s].append(s)

        # res = []    
        # for key in anagrams:
        #     res.append(anagrams[key])
        
        # return res
        ## instead of this I can just do 
        return list(anagrams.values())

        ## time complexity: O(n * k logk) (where k is the largest string)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(strs) <= 1: return [strs]

        # res = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26 ## rather than sorting every string, we can count array
        #     for char in s:
        #         count[ord(char) - ord("a")] += 1
        #     res[tuple(count)].append(s)
        
        # return list(res.values())
        
        
