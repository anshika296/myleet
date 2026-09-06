class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        max_length=0
        for i in set1: #
            if (i-1) not in set1:
                length=0 
                while(i+length) in set1: #we do i+0,i+1...
                    length+=1
                max_length=max(length,max_length)
        return max_length
        #o(n)