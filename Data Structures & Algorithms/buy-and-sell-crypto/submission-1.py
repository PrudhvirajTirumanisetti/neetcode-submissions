class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        purchaseDay = 0
        for currentDay in range(1, len(prices)):
            if prices[currentDay]<prices[purchaseDay]:
                purchaseDay = currentDay
            maxProfit = max( maxProfit, prices[currentDay]-prices[purchaseDay])
        return maxProfit