#You are given an array of strings words.
#Each element of words consists of two lowercase English letters.

#Create the longest possible palindrome by selecting some elements
#from words and concatenating them in any order.
#Each element can be selected at most once.

#Return the length of the longest palindrome that you can create.
#If it is impossible to create any palindrome, return 0.

#A palindrome is a string that reads the same forward and backward.

#Input: words = ["ab","ty","yt","lc","cl","ab"]
#Output: 8
#Explanation: One longest palindrome is
#"ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.

from collections import Counter
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        list1=Counter(words)
        if len(words)==1:
           return 2 if all(i[0] == i[1] for i in list1.keys()) else 0
        res=0
        count=1
        print(list1)
        s=set()
        for i in list1.keys():
            if i[::-1] in s:
              s.remove(i[::-1])
              res=res+(min(list1[i],list1[i[::-1]])*2)
            else:
                if i[0]==i[1]:
                    if list1[i]%2==0:
                        res+=list1[i]
                    else:
                        if list1[i]==1 and count==1:
                            res+=1
                            count-=1
                        else:
                            if count==1:
                                res=res+list1[i]
                                count-=1
                            else: res+=+list1[i]-1
                s.add(i)
        #if len(d)!=1 and all(x==list(d.values())[0] for x in d.values()): return 0
        return res*2

words = ["bb","bb"]
print(Solution().longestPalindrome(words))
