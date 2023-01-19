class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices)==1: return 0
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
                    




prices =[3,2,6,5,0,3]
out=Solution().maxProfit(prices)
print(out)
