class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs ==['']:
            return ""
        if not strs[0]:
            return ""
        s=[]
        a=0
        f=strs[0][a]
        n=len(strs[0])-1
        if len(strs)==1 and n==0: return f
        while n!=-1:
            for i in range(1, len(strs)):
                if f in strs[i]:
                    if f not in s:
                        s.append(f)
                else:
                    if f in s:
                        s.remove(f)
                    else: f=''
                    
            
            if n!=0:
             a+=1
             f=f+strs[0][a]
            n-=1
        t=s
        print(t)
        s=sorted(s)

        if s :return s[-1]
        else :return ''

strs = ["flower","flower","flower","flower"]
out=Solution().longestCommonPrefix(strs)
print(out)
