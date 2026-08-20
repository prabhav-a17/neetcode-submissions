class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        nei=defaultdict(list)
        if endWord not in wordList:
            return 0

        for word in wordList:
            for i in range(len(word)):
                pattern= word[:i]+'*'+word[i+1:]
                nei[pattern].append(word)
        visited=set(beginWord)
        q=collections.deque()
        q.append(beginWord)
        res=1

        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern= word[:i]+'*'+word[i+1:]
                    for neWord in nei[pattern]:
                        if neWord not in visited:
                            visited.add(neWord)
                            q.append(neWord)
            res+=1
        return 0
                
