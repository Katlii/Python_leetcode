"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path
between any two nodes in a tree.

This path may or may not pass through the root.

The length of a path between two nodes is represented by the number
of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
         if not root: return 0
         d={None:-1}
         stack=[root]
         res=0
         while stack:
              node=stack[-1]
              if node.left in d and node.right in d:
                   stack.pop()
                   left=d[node.left]+1
                   right=d[node.right]+1
                   d[node]=max(left,right)
                   res=max(res, left+right)
              else:
                   if node.left: stack.append(node.left)
                   if node.right: stack.append(node.right)
         return res
                   
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.left=TreeNode(-9)
root.right.right=TreeNode(-3)
root.right.left.right=TreeNode(9)
root.right.left.left=TreeNode(-7)
root.right.left.left.left=TreeNode(6)
root.right.left.left.right=TreeNode(-6)


print(Solution().diameterOfBinaryTree(root))
