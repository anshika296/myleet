class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for i in range(32):
            bit=n&1 #gives the last bit
            result=(result<<1)|bit #make space
            n=n>>1 #discard bit as its alr processed
        return result