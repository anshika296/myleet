import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        heap=[]
        for num,freq in count.items():
            heapq.heappush(heap,(freq,num)) #its freq,num not num,freq okayyy THATS THE TRICK
            if len(heap)>k:
                heapq.heappop(heap) #going to remove smallest freq ele because heap[0] will always be smallest freq ele
        result=[]
        for ele in heap:
            result.append(ele[1])#because num is the second ele 
        return result

            
        
        
        