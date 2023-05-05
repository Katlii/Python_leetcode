#Given a string s, find the length of the longest substring
#without repeating characters.

#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       maxx =0
       substring=[]
       for i, j in enumerate(s):
           if j in substring:
               index=substring.index(j)
               del substring [:index+1]
               substring.append(j)

           else:
               substring.append(j)
               maxx=max(maxx, len(substring))
       return maxx


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
