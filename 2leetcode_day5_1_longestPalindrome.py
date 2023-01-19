from collections import Counter
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        d={}
        summ=0
        for i in words:
            d[i]=Counter(i)
        for i in d:
            for j in d[i]:
                summ+=d[i][j]
        return summ

words = ["ab","ty","yt","lc","cl","ab"]
out=Solution().longestPalindrome(words)
print(out)
