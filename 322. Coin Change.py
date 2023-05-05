class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize dp array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # Loop through denominations and amounts
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # Check if amount can be made up
    
        return dp[amount] if dp[amount] != float('inf') else -1



coins = [186,419,83,408]
amount = 6249
print(Solution().coinChange(coins, amount))
