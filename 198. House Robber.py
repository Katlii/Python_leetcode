class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        res=0
        coins.sort()
        if amount==0: return 0
        for i in range(len(coins)-1, -1, -1):
            res+=amount//coins[i]
            amount=amount%coins[i]
        if amount!=0: return -1
        return res

nums=[186,419,83,408]
c=6249
print(Solution().coinChange(nums, c))
