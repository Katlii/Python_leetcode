import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s=list(s)
        d={}
        count, minn=0,0
        for i in s:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for j in d:
            a=d[j]
            if a%2==0:
                count+=a
            else:
                count+=a
                minn+=1
        return count-minn+1 if minn!=0 else count


s='bb'
out=Solution().longestPalindrome(s)
print(out)
