class Solution:
    def minCostClimbingStairs(self, coast: list[int]) -> int:
        B, pos=[], []
        s=set()
        a=0
        while a!=len(coast):
            if a==len(coast)-3:
                if coast[a+2]<=coast[a+1]:
                    s.add(a+2)
                    
                    return self.summ(coast, s)
                else:
                    s.add(a+1)
                    return self.summ(coast, s)
            elif a==len(coast)-2:
                return self.summ(coast, s)
            elif a==len(coast)-1:
                return self.summ(coast, s)
            else:        
                for i in range (a, a+2):
                    j=i+1
                    for j in range(j, i+3):
                        B.append(coast[i]+coast[j])
                        pos.append((i,j))
                minn=B[0]
                tmp=0
                for k in range(1, len(B)):
                    if minn>=B[k]:
                        minn=B[k]
                        tmp=k
                s.add(pos[tmp][0])
                s.add(pos[tmp][1])
                a=pos[tmp][1]
                B=[]
                pos=[]
    def summ(self, coast, s):
        summ=0
        for i in s:
            summ+=coast[i]
        return summ


coast=[1,100,1,1,1,100,1,1,100,1]
out=Solution().minCostClimbingStairs(coast)
print(out)
