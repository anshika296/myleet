class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones=[-s for s in stones] #because maxheap doesnt exist in python so we put -numbers
        heapq.heapify(stones)
        while len(stones)>1:
            first=abs(heapq.heappop(stones)) #this pops largest ele which is smallest
            second=abs(heapq.heappop(stones))#this pops second largest ele
            if first!=second:
                heapq.heappush(stones,-(first-second))
        if stones:
            return abs(stones[0])
        else:
            return 0


        