class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max=nums[0]
        current_min=nums[0]
        maxprod=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0: #if its negative
                current_min,current_max=current_max,current_min #we swap 
            current_max=max(nums[i],current_max*nums[i]) # because negative*negative gives positive
            current_min=min(nums[i],current_min*nums[i])
            maxprod=max(maxprod,current_max)
        return maxprod
