import copy
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isBalanced(self, root):
        leftH=self.Height(root.left)
        rightH=self.Height(root.right)
        print(leftH, rightH)
        if abs(leftH-rightH)<=1: return True
        else: return False

    def Height(self, root):
        if root is None:  return 0
        leftheight = self.Height(root.left)
        rightheight=self.Height(root.right)
        return max(leftheight, rightheight) + 1
 
root=TreeNode(3)
root.left=TreeNode(9)

root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
root.right.left.right=TreeNode(90)
print(Solution().isBalanced(root))
