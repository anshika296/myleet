class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l=l-1
                r=r+1
            return s[l+1:r] #After the loop stops, l and r are one position outside the palindrome. l+1 brings us back inside, while r is already the correct exclusive slicing boundary.
        max_p=""
        for i in range(len(s)):
            p1=expand(i,i)#odd
            p2=expand(i,i+1)#even
            if len(p1)>len(max_p):
                max_p=p1
            if len(p2)>len(max_p):
                max_p=p2
        return max_p
        