class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binsearch(nums,target,True)
        right=self.binsearch(nums,target,False)
        return [left,right]
    def binsearch(self,nums,target,leftbias):
        left=0
        right=len(nums)-1
        i=-1
        while left<=right:
            mid=(left+right)//2
            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            else:
                i=mid
                if leftbias:
                    right=mid-1
                else:
                    left=mid+1
        return i

