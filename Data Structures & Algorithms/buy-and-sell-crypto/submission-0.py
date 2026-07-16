class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # I need to check prices daily about how much profit am I earning today.
        # And after that I check if the current sell price is less than the minimum buy price

        lowestPrice = prices[0]
        maxProfit = prices[0] - lowestPrice

        for i in range(len(prices)):
            # I will now check profit daily
            todaysPrice = prices[i]
            todaysProfit = todaysPrice - lowestPrice
            if todaysProfit > maxProfit:
                # since todays profit is higher we will change maxProfit to it
                maxProfit = todaysProfit
            
            # Now Lets check cheapest price before today
            if todaysPrice < lowestPrice:
                lowestPrice = todaysPrice
            
        return maxProfit