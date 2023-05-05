"""
You are given an integer array coins representing coins of
different denominations and an integer amount representing a
total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,return -1.

You may assume that you have an infinite number of each kind of coin.
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        def rec(i,rsum ):
            if(rsum==0): return True
            if(i==len(nums) or rsum < 0): return False 
            elif(self.dp[i][rsum] != -1 ):
                return self.dp[i][rsum]
            self.dp[i][rsum]= rec(i+1,rsum-nums[i]) or rec(i+1,rsum)
            return self.dp[i][rsum]
        
        
        totalsum = sum(nums)
        if(totalsum%2): return False 
        else: 
            self.dp = [ [-1]*((totalsum//2)+1) for _ in range(len(nums))]
            return rec(0,totalsum//2)


        """res1, res2= [], []
        s=sum(nums)
        lenght=len(nums)
        if s%2 != 0: return False
        ost, H =s//2, s//2
        res1.append(nums[0])
        ost-=nums[0]
        u=2
        for i in range(1,lenght):
            if ost>=nums[i]:
                res1.append(nums[i])
                ost-=nums[i]
            u=i+1
            while u!=lenght:
                for j in range(u, lenght):
                    if ost>=nums[j]:
                        res1.append(nums[j])
                        ost-=nums[j]
                if sum(res1)==H:
                    for a in res1:
                        d=nums.index(a)
                        del nums[d]
                    if sum(nums)==H: return True
                    else: return False
                else:
                    u+=1
                    res1=[nums[0], nums[i]]
                    ost=H-sum(res1)
            res1=[nums[0]]
            ost=H-nums[0]
        return False
        """
                


nums = [1,4,3,2,8]
print(Solution().canPartition(nums))
