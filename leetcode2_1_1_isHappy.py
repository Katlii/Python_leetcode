class Solution:
    def isHappy(self, n: int) -> bool:
        summ=0
        s=set()
        while n!=1:
            n=sum(int(i)**2 for i in str(n))
            if n not in s:
                s.add(n)
            else: return False
        return True


n=2
out=Solution().isHappy(n)
print(out)
