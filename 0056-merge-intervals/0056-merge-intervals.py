class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0]) #first sort then do prev=intervals[0]
        result=[]
        prev=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=prev[1]:
                prev=[prev[0],max(prev[1],intervals[i][1])]
            else:
                result.append(prev)
                prev=intervals[i]
        result.append(prev)
        return result
        