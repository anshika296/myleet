class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[1]*n
        parent=[-1]*n
        max_length=1
        last=0
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i] and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    parent[i]=j
            if dp[i]>max_length:
                max_length=dp[i]
                last=i
        lis=[]
        while last!=-1:
            lis.append(nums[last])
            last=parent[last]
        lis.reverse()
        return max_length
        