class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm={}
        for i in s:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        for j in range(len(s)):
            if hm[s[j]]==1:
                return j
                break        
        return -1
        