class Solution:
    def climbStairs(self, n): 
        count = 0
        d = {}
        for i in range(0, n+1):
            for j in range(0, (n//2)+1):
                if i + 2*j == n and i+j not in d:
                    d[i+j] = "" 
                    count = self.factorial(i+j)/(self.factorial(i)*self.factorial(j)) + count
        return count
    def factorial(self, x):
        if x != 0:
            return x*self.factorial(x-1)
        else:
            return 1
        

n=6
out=Solution().climbStairs(n)
print(out)
