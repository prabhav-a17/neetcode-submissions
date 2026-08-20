import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       #Ok so first I need to calculate the euclidean distance for each of them
       #Then I can use heapify to sort these and then I will pop the top k elements
       res=[]
       euclid=[]
       for point in points:
            x=point[0]
            y=point[1]
            euclid.append(((math.sqrt((x**2)+(y**2))), point))
        
       heapq.heapify(euclid)
       while k:
            dist, point = heapq.heappop(euclid)
            res.append(point)
            k-=1
       return res


    