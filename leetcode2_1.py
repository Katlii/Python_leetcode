class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        d={}
        d[s[0]]=t[0]
        del s[0]
        del t[0]
        for i,x in enumerate(s):
            if x not in d:
                l=len(d)
                while l!=0:
                    for j in d:
                        if t[i] not in d[j]:
                            l-=1
                        else: return False
                d[x]=t[i]

                        
            else:
                if t[i]!=d[x]:
                    return False
        return True
            
            



s='egcd'
t='adfd'
out=Solution().isIsomorphic(s, t)
print(out)
