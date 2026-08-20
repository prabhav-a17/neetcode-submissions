from collections import defaultdict
class Twitter:

    def __init__(self):
        #initializes the twitter object
        self.count=0
        self.followMap=defaultdict(set)
        self.tweetMap=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count-=1 # because we are using minheap 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #Fetches at most 10 recent tweets each item should only be with followers or themselves
        res=[]
        minHeap=[]

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index=len(self.tweetMap[followeeId])-1
                count, tweetId= self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        while minHeap and len(res)<10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >=0:
                count, tweetId= self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        #Ok so for this I am thinking a hashset bc lookup times are O(1) 
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Ok for this I am thinking a hashset again 
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
