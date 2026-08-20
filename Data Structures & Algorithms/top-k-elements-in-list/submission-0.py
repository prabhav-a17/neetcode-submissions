class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        result = []
        
        for x in nums:
            if x in freq_dict:
                freq_dict[x] += 1
            else:
                freq_dict[x] = 1
        newList= sorted(freq_dict, key=freq_dict.get, reverse=True)
        result= newList[:k]
        return result
        


            

        