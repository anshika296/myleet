import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/mid) #round it off
            if hours<=h:
                res=min(res,mid)
                r=mid-1 #search thru left
            else:
                l=mid+1
        return res



        