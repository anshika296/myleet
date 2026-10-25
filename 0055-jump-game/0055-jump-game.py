class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest=0
        for i in range(len(nums)):
            if i>farthest: #This checks whether the current index is beyond your reach.
                return False
            farthest=max(farthest,i+nums[i])
        return True #basically u reached end of list