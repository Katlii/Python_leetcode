# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]):
        total=len(nums)
        if not total:
            return None
        middle=total//2
        return TreeNode (
            nums[middle],
            self.sortedArrayToBST(nums[:middle]),
            self.sortedArrayToBST(nums[middle+1:]))

nums = [-20,-10,-3,0,5,9,11]
print(Solution().sortedArrayToBST(nums))
