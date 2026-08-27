class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF #forces integer to stay within 32 bits
        max_int=0x7FFFFFFF
        while(b!=0):
            carry=(a&b)<<1 
            a=(a^b)&mask
            b=carry&mask
        if a<=max_int:
            return a #a is positive
        else:
            a=~(a^mask) #converts the number back to the negative python number
            return a
        