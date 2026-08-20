class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for x in strs:
            newX = ''.join(sorted(x))
            if newX not in anagrams:
                anagrams[newX] = [x]
            else: 
                anagrams[newX].append(x)
        return list(anagrams.values())


            
        