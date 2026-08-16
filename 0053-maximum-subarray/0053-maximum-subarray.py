class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        best_sum=nums[0]
        for i in range(len(nums)):
            current_sum+=nums[i]
            if current_sum>best_sum:
                best_sum=current_sum
            if current_sum<0:
                current_sum=0
        return best_sum

        


        