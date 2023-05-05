#Given an integer array nums, find a subarray
#that has the largest product, and return the product.

#Input: nums = [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.

from collections import deque
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        L=len(nums)
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        for i in range(1, L):
            tmp_max = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            tmp_min = min(nums[i], max_prod*nums[i], min_prod*nums[i])
            max_prod, min_prod = tmp_max, tmp_min
            result=max(result, max_prod)

        return result



nums = [2,3,-2,4,4]
print(Solution().maxProduct(nums))
