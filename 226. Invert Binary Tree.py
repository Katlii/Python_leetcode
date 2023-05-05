#Given the root of a binary tree, invert the tree, and return its root.
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root):
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

root=TreeNode(1)
root.right=TreeNode(10)
root.left=TreeNode(2)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right.left=TreeNode(6)
root.right.right=TreeNode(9)
out=Solution().invertTree(root)
print(out)

