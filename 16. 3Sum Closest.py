#Given an integer array nums of length n and an integer target,
#find three integers in nums such that the sum is closest to target.

#Return the sum of the three integers.
#Input: nums = [-1,2,1,-4], target = 1
#Output: 2
#Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums=sorted(nums)
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum > target:
                    right -= 1
                else:
                    left += 1
        return closest_sum


nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
print(Solution().threeSumClosest(nums, target))
