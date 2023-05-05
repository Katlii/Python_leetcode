class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        d={}
        for i, j in enumerate(zip(*strs)):
            d[i]=j
        s=''
        for i in d:
            if all(x==d[i][0] for x in d[i]):
                s+=d[i][0]
            else: return s
        return s
        
                    
            
strs=["cir","car"]
print(Solution().longestCommonPrefix(strs))

