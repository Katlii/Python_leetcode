class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        d=[]
        position=0
        for i in s:
            for j in range(position, len(t)):
                if i==t[j]:
                    d.append(position)
                    position+=1
                    break
                position+=1
        if len(d)==len(s):
            return True
        else: return False
                    




s='abx'
t='ahbgdc'
out=Solution().isSubsequence(s, t)
print(out)
