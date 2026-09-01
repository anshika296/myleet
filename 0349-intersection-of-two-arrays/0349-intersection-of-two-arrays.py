class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        result=set()#making a set cuz we dont want repeating element
        for i in nums2:
            if i in set1:
                result.add(i)
        return list(result)