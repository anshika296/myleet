class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_greater={}
        result=[]
        for i in nums2:
            while stack!=[] and i>stack[-1]:
                prev=stack.pop()
                next_greater[prev]=i
            stack.append(i)
        for x in stack:
            next_greater[x]=-1
        for i in nums1:
            result.append(next_greater[i])
        return result
                