class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowestPrice = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            todaysPrice = prices[i]
            todaysProfit = todaysPrice - lowestPrice
            if todaysProfit > maxProfit:
                maxProfit = todaysProfit
            if todaysPrice < lowestPrice:
                lowestPrice = todaysPrice
            
        return maxProfit