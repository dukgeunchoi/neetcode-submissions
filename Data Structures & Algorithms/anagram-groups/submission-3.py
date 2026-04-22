class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## instead of sorting, we can make it more efficient
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())


        
        # anagrams = defaultdict(list)

        # for s in strs:
        #     sorted_s = "".join(sorted(s)) ## O(nlogn)
        #     anagrams[sorted_s].append(s)

        # # res = []    
        # # for key in anagrams:
        # #     res.append(anagrams[key])
        
        # # return res
        # ## instead of this I can just do 
        # return list(anagrams.values())

        # ## time complexity: O(n * k logk) (where k is the largest string)

