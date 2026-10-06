class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0#because in binary numbers have only one 1 and when multiply with other numbers
        