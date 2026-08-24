class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid=0
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]: #we compare with right
                left=mid+1
            else:
                right=mid #it cud be the mid ele
        return nums[left] #because its sorted
        