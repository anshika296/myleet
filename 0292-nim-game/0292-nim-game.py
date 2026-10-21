class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4!=0 #theres a pattern where every multiple of 4,opponent wins
        