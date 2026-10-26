class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(3)]
        for f in range(1,n+1):
            dp[1][f]=f
        for i in range(1,3):
            dp[i][1]=1
        for i in range(2,3):
            for f in range(2,n+1):
                best=float('inf')
                for x in range(1,f+1):
                    breaks=dp[i-1][x-1]
                    survives=dp[i][f-x]
                    best=min(best,1+max(breaks,survives))
                dp[i][f]=best
        return dp[2][n]
                



        