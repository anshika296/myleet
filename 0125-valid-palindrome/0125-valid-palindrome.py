class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        clean=""
        for i in s:
            if i in "1234567890" or i in "abcdefghijklmnopqrstuvwxyz":
                clean+=i
        l=0
        r=len(clean)-1
        if len(clean)==0:
            return True
        for i in range(l,r):
            if clean[l]!=clean[r]:
                  return False
                  break
            else:
                  l=l+1
                  r=r-1
        return True
        
        