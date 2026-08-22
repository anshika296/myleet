class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #max_length=0
        #for i in range(len(s)):
        #   result=set()
        #   for j in range(i,len(s)):
        #       if s[j] in result:
        #           break
        #       result.add(s[j])
        #       max_length=max(max_length,j-i+1)
        #return max_length
        result=set()
        left=0
        max_length=0
        for right in range(len(s)):
            while s[right] in result: #abba #o(n) o(n)
                # we shrink
                result.remove(s[left])
                left=left+1
            result.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length


