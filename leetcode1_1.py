class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        A=[]
        A.append(nums[0])
        for x in range (1, len(nums)):
            b=A[x-1]+nums[x]
            A.append(b)
            b=0
        return A


nums = [1,2,3,4]
print(Solution().runningSum(nums))
 
