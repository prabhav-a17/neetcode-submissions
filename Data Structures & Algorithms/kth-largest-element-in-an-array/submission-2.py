class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsinv=[]
        for i in nums:
            numsinv.append(-i)
        heapq.heapify(numsinv)
        while k-1:
            heapq.heappop(numsinv)
            k-=1
        res= heapq.heappop(numsinv)
        return -res