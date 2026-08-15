class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm={}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        mj=0
        mj_ele=nums[0]
        for i in hm:
            if hm[i]>mj:
                mj=hm[i]
                mj_ele=i
        return mj_ele


        