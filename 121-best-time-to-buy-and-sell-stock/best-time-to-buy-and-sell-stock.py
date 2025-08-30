class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp =  0
        bestbuy = prices[0]
        for i in range(len(prices)):
            if(prices[i]>bestbuy):
                maxp = max(maxp,prices[i]-bestbuy)
            bestbuy = min(bestbuy,prices[i])
        return maxp
