class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        purchaseDay = 0
        for index in range(1, len(prices)):
            if prices[index]<prices[purchaseDay]:
                purchaseDay = index
            maxProfit = max( maxProfit, prices[index]-prices[purchaseDay])
        return maxProfit