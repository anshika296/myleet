class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1=''
        for i in digits:
            str1+=str(i)
        num=int(str1)
        num=num+1
        res=[]
        while num>0:
            dig=num%10
            res.append(dig)
            num=num//10
        return res[::-1]


            

        