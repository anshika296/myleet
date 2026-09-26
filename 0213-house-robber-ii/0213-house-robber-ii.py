class Solution:
    def rob_line(self,nums):
        prev2=0
        prev1=0
        for money in nums:
            current=max(prev1,prev2+money)
            prev2=prev1#this is old value
            prev1=current#rmb this is just like dp[i-1]
        return prev1
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob_line(nums[1:]),self.rob_line(nums[:-1]))
   
       
        