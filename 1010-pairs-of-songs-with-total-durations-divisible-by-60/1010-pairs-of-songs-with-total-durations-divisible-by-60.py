class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count=0
        freq={}
        for i in time:
            r=i%60
            complement=(60-r)%60
            if complement in freq:
                count+=freq[complement]
            freq[r]=freq.get(r,0)+1
        return count