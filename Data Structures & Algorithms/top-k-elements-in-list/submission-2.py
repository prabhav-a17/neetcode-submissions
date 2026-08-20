class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Ok for this I am pretty sure we should be creating buckets like we get the count of each unique number in nums and then we then loop through that and create buckets and then if the bucket isnt empty add to our results list

        counts= Counter(nums)
        buckets = [[] for x in range(len(nums)+1)]
        for x in counts:
            buckets[counts[x]].append(x)

        res=[]
        for x in buckets[::-1]:
            for y in x:
                res.append(y)
                if len(res)==k:
                    return res