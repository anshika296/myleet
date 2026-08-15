class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        profit=0
        for right in range(1,len(prices)):
            if prices[right]<prices[left]:
                left=right
            diff=prices[right]-prices[left]
            if diff>profit:
                profit=diff
        return profit
        