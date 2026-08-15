class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        if num<0:
            return False
        else:
            rev=0
            while(num>0):
                last=num%10
                rev=rev*10+last
                num=num//10   
            if rev==x:
                return True  
            else:
                return False
        